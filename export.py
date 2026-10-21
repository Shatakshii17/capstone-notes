import csv

# columns from data_notes.csv
FIELDS = ["run_id", "fastener_id", "material", "signal_peak", "classification"]


def export_results(results, filename="results.csv"):
    # results is a list of dicts, one per fastener
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in results:
            # data notes say every exported row needs a classification
            if "classification" not in row:
                print("skipping row, no classification:", row)
                continue
            writer.writerow(row)


if __name__ == "__main__":
    # fake rows just to test that it works
    test_results = [
        {"run_id": 1, "fastener_id": "T01", "material": "Titanium",
         "signal_peak": 0.82, "classification": "Titanium"},
        {"run_id": 1, "fastener_id": "I01", "material": "Inconel",
         "signal_peak": 1.12, "classification": "Inconel"},
    ]
    export_results(test_results)
    print("exported", len(test_results), "rows")
