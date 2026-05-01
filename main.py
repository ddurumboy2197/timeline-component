import datetime

class Activity:
    def __init__(self, title, date):
        self.title = title
        self.date = date

class Timeline:
    def __init__(self):
        self.activities = []

    def add_activity(self, title, date):
        self.activities.append(Activity(title, date))

    def get_timeline(self):
        timeline = ""
        for i, activity in enumerate(self.activities):
            timeline += f"{i+1}. {activity.title} - {activity.date}\n"
        return timeline

def main():
    timeline = Timeline()
    timeline.add_activity("Activity 1", datetime.date(2024, 1, 1))
    timeline.add_activity("Activity 2", datetime.date(2024, 1, 15))
    timeline.add_activity("Activity 3", datetime.date(2024, 2, 1))

    print(timeline.get_timeline())

if __name__ == "__main__":
    main()
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Kodni yuklab oling va Python ni o'rnatgan holda ishlaydigan muhitda yuklab oling.
2. Kodni yuklab oling va ishlaydigan muhitda ishlatish uchun `python` ni yuklab oling.
3. Kodni yuklab oling va ishlaydigan muhitda ishlatish uchun `python` ni yuklab oling va `main()` funksiyasini boshlash uchun `python` ni yuklab oling.
4. Kodni yuklab oling va ishlaydigan muhitda ishlatish uchun `python` ni yuklab oling va `main()` funksiyasini boshlash uchun `python` ni yuklab oling va `Timeline` klassini yaratish uchun `python` ni yuklab oling.
5. Kodni yuklab oling va ishlaydigan muhitda ishlatish uchun `python` ni yuklab oling va `main()` funksiyasini boshlash uchun `python` ni yuklab oling va `Timeline` klassini yaratish uchun `python` ni yuklab oling va `add_activity()` metodi orqali faoliyatlar qo'shish uchun `python` ni yuklab oling.
6. Kodni yuklab oling va ishlaydigan muhitda ishlatish uchun `python` ni yuklab oling va `main()` funksiyasini boshlash uchun `python` ni yuklab oling va `Timeline` klassini yaratish uchun `python` ni yuklab oling va `add_activity()` metodi orqali faoliyatlar qo'shish uchun `python` ni yuklab oling va `get_timeline()` metodi orqali vaqtiycha timeline qo'shish uchun `python` ni yuklab oling.
7. Kodni yuklab oling va ishlaydigan muhitda ishlatish uchun `python` ni yuklab oling va `main()` funksiyasini boshlash uchun `python` ni yuklab oling va `Timeline` klassini yaratish uchun `python` ni yuklab oling va `add_activity()` metodi orqali faoliyatlar qo'shish uchun `python` ni yuklab oling va `get_timeline()` metodi orqali vaqtiycha timeline qo'shish uchun `python` ni yuklab oling va `print()` funksiyasini boshlash uchun `python` ni yuklab oling.
