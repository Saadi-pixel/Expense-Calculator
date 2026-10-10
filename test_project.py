import csv
import project

def test_calculate_total(capsys):
    with open(project.filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Food", "Pizza", "2026-10-10", "100"])
        writer.writerow(["Travel", "Bus", "2026-10-11", "50"])
    
    project.calculate_total()
    captured = capsys.readouterr()
    assert "150" in captured.out


def test_calculate_categorywise_spendings(monkeypatch, capsys):
    with open(project.filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Food", "Burger", "2026-10-10", "200"])
        writer.writerow(["Food", "Coffee", "2026-10-11", "50"])
        
    monkeypatch.setattr("builtins.input", lambda _: "Food")
    project.calculate_categorywise_spendings()
    captured = capsys.readouterr()
    assert "250" in captured.out


def test_search_expense(monkeypatch, capsys):
    with open(project.filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Travel", "Train Ticket", "2026-10-10", "500"])
        
    monkeypatch.setattr("builtins.input", lambda _: "Travel")
    project.search_expense()
    captured = capsys.readouterr()
    assert "Train Ticket" in captured.out
