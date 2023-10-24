import pandas as pd
from tqdm import tqdm
import multiprocessing
from joblib import Parallel, delayed
from pickle import PicklingError

from . import xpd


def x_on_iter(llist, calc_func, total=None, clear_nones=False, flatten=False, backend=None, n_jobs=-1):
    if total is None:
        try:
            total = len(llist)
        except TypeError:
            total = None

    if n_jobs == 1:
        all_items = [calc_func(i) for i in tqdm(llist, total=total)]

    else:
        xtqdm = x_tqdm(llist, total=total, n_jobs=n_jobs)
        try:
            all_items = Parallel(backend=backend, n_jobs=n_jobs)(delayed(calc_func)(i) for i in xtqdm)
        except PicklingError:
            if backend != 'threading':
                print("NOTE: PicklingError might get resolved by switching to 'threading' backend")
            raise

        xtqdm.finished()

    if clear_nones:
        all_items = [i for i in all_items if i is not None]

    if flatten:
        all_items = [item for sublist in all_items for item in sublist]

    return all_items


def x_on_dict_keys(ddict, keys, func, backend=None, n_jobs=-1):
    all_keys = list(keys)
    xtqdm = x_tqdm(all_keys, total=len(all_keys))
    all_vals = Parallel(backend=backend, n_jobs=n_jobs)(delayed(func)(ddict[k]) for k in xtqdm)
    xtqdm.finished()
    new_dict = dict(zip(all_keys, all_vals))
    return new_dict


def x_on_keys(keys, func, backend=None, n_jobs=-1):
    all_keys = list(keys)
    xtqdm = x_tqdm(all_keys, total=len(all_keys))
    all_vals = Parallel(backend=backend, n_jobs=n_jobs)(delayed(func)(k) for k in xtqdm)
    xtqdm.finished()
    new_dict = dict(zip(all_keys, all_vals))
    return new_dict


def x_iter_groups_p(get_row, df, on, dropna=True, sort_on=None, return_df=True, n_jobs=-1):
    """
    A wrapper around xpd.x_iter_groups() that runs `calc_func` in parallel, generating a df on the results.

    example: xparallel.x_iter_groups_p(df, 'key', get_row)

    Notes:
        - get_row's signature is: get_row(dfg, keys, gtitle)
        - get_row() can return either a pd.Series or a list of such series.
    """

    if sort_on:
        print(f"Warning (x_iter_groups_p): sorting (on {sort_on}) should probably be moved inside worker")

    iter = xpd.x_iter_groups(df, on, dropna=dropna, df_only=False, yield_total=True, with_tqdm=False, sort_on=sort_on)
    total = next(iter)

    rows = x_on_iter(iter, lambda i: get_row(*i), total=total, clear_nones=True, n_jobs=n_jobs)

    if len(rows):
        if isinstance(rows[0], list):
            rows = [row for sublist in rows for row in sublist]

    if return_df:
        row0 = rows[0]
        if isinstance(row0, dict):
            rows = [pd.Series(r) for r in rows]

        row0 = rows[0]
        if isinstance(row0, pd.Series):
            df = pd.DataFrame(rows)

        elif isinstance(row0, pd.DataFrame):
            df = pd.concat(rows, ignore_index=True)

        return df

    return rows


def x_reduce(llist, calc_func, reduce_func=max, backend=None, n_jobs=-1):
    vals = x_on_iter(llist, calc_func, backend=backend, n_jobs=n_jobs)
    vals = [v for v in vals if v is not None]
    val = reduce_func(vals)
    return val


def x_params(calc_func, *args, **kwargs):
    """ Needed to avoid parallelization issue """
    return calc_func, args, kwargs


def x_build_df_from_row_gen(row_gen, backend=None, n_jobs=-1):
    """
    Builds a df from a row generator (useful when there is a complicated loop that needs parallelization)
    The row generator has the form:
    def row_gen():
        for ...:
            # instead of calc_func(arg1, arg2, kw1=1, kw2=2)
            yield xparallel.x_params(calc_func, arg1, arg2, kw1=1, kw2=2)

    df = xparallel.x_build_df_from_row_gen(row_gen)
    """

    if n_jobs == 1:
        rows = [rg(*args, **kwargs) for rg, args, kwargs in row_gen()]

    else:
        try:
            rows = Parallel(backend=backend, n_jobs=n_jobs)(delayed(rg)(*args, **kwargs) for rg, args, kwargs in row_gen())
        except PicklingError:
            if backend != 'threading':
                print("NOTE: PicklingError might get resolved by switching to 'threading' backend")
            raise

    rows = [i for i in rows if i is not None]
    df = pd.DataFrame(rows)
    return df


class x_tqdm(tqdm):
    """
    tqdm that handles parallel jobs better
    """

    def __init__(self, *args, n_jobs=1, **kwargs):
        if n_jobs == -1:
            n_jobs = multiprocessing.cpu_count()

        self.n_jobs = n_jobs
        self.is_finished = False
        super().__init__(*args, **kwargs)

    def finished(self):
        self.is_finished = True
        self.refresh()
        self.close()

    def close(self):
        pass

    def do_close(self):
        super().close()

    @property
    def format_dict(self):
        fd = super().format_dict

        if not self.is_finished:
            fd['n'] = max(fd['n']-self.n_jobs, 0)
        return fd


if __name__ == "__main__":
    import time
    x = x_tqdm(list(range(8)), n_jobs=2)
    Parallel(n_jobs=2)(delayed(lambda i: time.sleep(2))(i) for i in x)
    x.finished()

    print('done')