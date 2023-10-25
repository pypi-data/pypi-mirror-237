def test_try_variable_from_list():
    from omlabs.helpers import try_variable_from_list

    vars_in_file = ["thetao", "so"]
    query_vars = ["temp", "ptemp", "thetao", "TEMP"]

    out = try_variable_from_list(vars_in_file, query_vars)

    assert isinstance(out, str)
    assert out == "thetao"

    query_vars = ["temp", "ptemp", "TEMP"]

    out = try_variable_from_list(vars_in_file, query_vars)

    assert out is None
