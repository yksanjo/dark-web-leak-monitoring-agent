from datetime import datetime, timezone


def main() -> None:
    print("dark-web-leak-monitoring-agent initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
