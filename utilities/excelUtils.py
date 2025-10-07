import openpyxl
import os

def get_login_data(excel_path, sheet_name=None):
    """
    Reads login data from the given Excel file and returns a list of tuples (username, password, exp).
    If sheet_name is provided, reads from that sheet; otherwise, uses the active sheet.
    Blank values are preserved and not filtered out, so tests can run with blank data as well.
    """
    workbook = openpyxl.load_workbook(excel_path)
    if sheet_name:
        sheet = workbook[sheet_name]
    else:
        sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
        # Always append the row, even if some values are blank/None
        data.append((row[0] if row[0] is not None else '',
                     row[1] if row[1] is not None else '',
                     row[2] if row[2] is not None else ''))
    return data
