import google.cloud.logging
from Database import Database

from committee_contributions import update_committee_contributions
from committee_expenditures import update_committee_expenditures


def main():
    client = google.cloud.logging.Client()
    client.setup_logging()

    db = Database()
    db.get_constants()
    # update_committee_contributions(db)
    update_committee_expenditures(db)


if __name__ == "__main__":
    main()
