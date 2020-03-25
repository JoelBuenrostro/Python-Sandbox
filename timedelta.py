from datetime import datetime, timedelta

now = datetime.now()

nextdate = now + timedelta(days=2)
pastdate = now - timedelta(weeks=3)

print(nextdate.date())
print(pastdate.date())