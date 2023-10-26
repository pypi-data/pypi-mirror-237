# Sample Test passing with nose and pytest
from pathlib import Path

import pytest
from tableauhyperapi import HyperException

import tests.conftest as ct
from tableau_helpers import hyper


def test_create_hyper_from_default_csv_path_obj(
    tmp_path, csv_path=ct.good_csv_path(), csv_schema=ct.good_csv_schema()
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    linecount = hyper.copy_csv_to_hyper(tmp_hyper_file, Path(csv_path), csv_schema)
    assert linecount == 2


def test_create_hyper_from_default_csv_path_str(
    tmp_path, csv_path=ct.good_csv_path(), csv_schema=ct.good_csv_schema()
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    linecount = hyper.copy_csv_to_hyper(tmp_hyper_file, Path(csv_path), csv_schema)
    assert linecount == 2


def test_create_hyper_from_default_tab_path_str(
    tmp_path, csv_path=ct.good_tab_path(), csv_schema=ct.good_csv_schema()
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    linecount = hyper.copy_csv_to_hyper(
        tmp_hyper_file, Path(csv_path), csv_schema, delimiter="\t"
    )
    assert linecount == 2


def test_fail_create_hyper_from_default_tab_path_str(
    tmp_path, csv_path=ct.good_tab_path(), csv_schema=ct.good_csv_schema()
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    with pytest.raises(HyperException):
        assert hyper.copy_csv_to_hyper(tmp_hyper_file, Path(csv_path), csv_schema)


def compare_columns(columns_a, columns_b):
    for x, y in zip(columns_a, columns_b):
        assert x.name == y.name
        assert x.nullability == y.nullability
        assert x.type == y.type
        assert x.collation == y.collation


def test_load_good_table_def(
    table_def_path=ct.good_table_def_path(), csv_schema=ct.good_csv_schema()
):
    table_def = hyper.load_table_defs(Path(table_def_path))
    assert table_def[0].table_name == csv_schema.table_name
    compare_columns(table_def[0].columns, csv_schema.columns)


def test_create_hyper_with_fact_table_str(
    tmp_path,
    csv_left=ct.good_left_path(),
    csv_right=ct.good_right_path(),
    csv_join_tabledef=ct.good_join_table_def_path(),
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    csvs = [Path(csv_left), Path(csv_right)]
    tabledef = hyper.load_table_defs(Path(csv_join_tabledef))
    linecount = hyper.copy_csv_to_hyper(tmp_hyper_file, csvs, tabledef)
    assert linecount == 4


def test_create_hyper_from_default_csv_doesnt_exist(
    tmp_path,
    doesnt_exist_path=ct.doesnt_exist_path(),
    good_csv_schema=ct.good_csv_schema(),
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    with pytest.raises(FileNotFoundError):
        assert hyper.copy_csv_to_hyper(
            tmp_hyper_file, Path(doesnt_exist_path), good_csv_schema
        )


def test_create_hyper_from_string_path(
    tmp_path,
    doesnt_exist_path=ct.doesnt_exist_path(),
    good_csv_schema=ct.good_csv_schema(),
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    with pytest.raises(TypeError):
        assert hyper.copy_csv_to_hyper(
            tmp_hyper_file, doesnt_exist_path, good_csv_schema
        )


def test_create_hyper_from_default_csv_with_header(
    tmp_path, good_csv_path=ct.good_csv_path(), good_csv_schema=ct.good_csv_schema()
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")
    linecount = hyper.copy_csv_to_hyper(
        tmp_hyper_file,
        Path(good_csv_path),
        good_csv_schema,
        header=True,
    )
    assert linecount == 1


def test_create_hyper_from_default_csv_bad_schema(
    tmp_path, good_csv_path=ct.good_csv_path(), bad_csv_schema=ct.bad_csv_schema()
):
    tmp_hyper_file = Path(tmp_path, "tmp.hyper")

    with pytest.raises(HyperException):
        assert hyper.copy_csv_to_hyper(
            tmp_hyper_file, Path(good_csv_path), bad_csv_schema
        )
