import os
import re
import pandas as pd
from bs4 import BeautifulSoup
from fake_headers import Headers
from flatten_any_dict_iterable_or_whatsoever import fla_tu
import requests
from a_pandas_ex_apply_ignore_exceptions import pd_add_apply_ignore_exceptions
import lxml
#import cchardet
pd_add_apply_ignore_exceptions()


def get_fake_header():

    header = Headers(headers=False).generate()
    agent = header["User-Agent"]

    headers = {
        "User-Agent": f"{agent}",
    }

    return headers


def get_html_src(htmlcode, fake_header=True):
    if isinstance(htmlcode, str):
        if os.path.exists(htmlcode):
            if os.path.isfile(htmlcode):
                with open(htmlcode, mode="rb") as f:
                    htmlcode = f.read()
        elif re.search(r"^.{1,10}://", str(htmlcode)) is not None:
            if not fake_header:
                htmlcode = requests.get(htmlcode).content
            else:
                htmlcode = requests.get(htmlcode, headers=get_fake_header()).content
    return htmlcode


def html_to_df(html, parser="lxml", fake_header=True, *args, **kwargs):
    data = get_html_src(html, fake_header)
    df = pd.concat(
        [
            pd.DataFrame(q.__dict__.items()).set_index(0).T
            for q in BeautifulSoup(data, parser).find_all()
        ],
        ignore_index=True,
    )
    df = df.loc[df.contents.ds_apply_ignore(pd.NA, lambda x: len(x) > 0)].reset_index(
        drop=True
    )
    df["attrs"] = df["attrs"].ds_apply_ignore(pd.NA, lambda x: tuple(fla_tu(x)))
    df["old_index"] = df.index.__array__().copy()
    df = df.explode("attrs").reset_index(drop=True)
    df["attrs"] = df["attrs"].ds_apply_ignore(
        (None, None), lambda x: ((x[0], x[1][0]) if not pd.isna(x) else (None, None))
    )
    dfc = pd.concat([pd.Series(x) for x in zip(*df["attrs"])], axis=1)
    dfc.columns = ["value", "key"]
    df = pd.concat([df, dfc], axis=1)
    df.columns = [f"aa_{x}" for x in df.columns]
    df = df.drop(
        columns=[
            "aa_parser_class",
            "aa_namespace",
            "aa__namespaces",
            "aa_prefix",
            "aa_known_xml",
            "aa_attrs",
            "aa_namespace",
            "aa_interesting_string_types",
            "aa_preserve_whitespace_tags",
            "aa_cdata_list_attributes",
            "aa_can_be_empty_element",
        ]
    )
    df = (
        df.fillna(pd.NA)
        .reset_index(drop=True)
        .rename(columns={"aa_old_index": "aa_element_index"})
    )
    return df


def pd_add_bs4_to_df_lite():
    pd.Q_bs4_to_df_lite = html_to_df
