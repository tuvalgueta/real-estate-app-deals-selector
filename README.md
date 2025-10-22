
You are and excel and VBA expert, the best one in the industry today.
learn the attached excel. stracture and data.

generate simple GUI that request in dialog box similar excel (with those 3 sheets) and fill in sheet 3 with relavant deals after he applyed the logic in the current python.
Each line is sheet "עסקאות נדל"ן" is a separate real estate transaction (starting from line 4,lines before are table headers).
Your goal is to reduce the number of comparison deals to the 7 most relevant deals according to the following criteria:
suggest the best approach to do that based on the existing columns in sheet "עסקאות נדל"ן"

Attached excel hold 2 sheets
sheet1 includes the property i want to compare with - for appraisal evaluation.
sheet2 include actual deals that need to add column with score for similarity to the property in sheet1.
Generate simple GUI that request in dialog box similar excel (with similar sheets and stracture) Your goal is to reduce the number of comparison deals to the 7 most relevant deals according to make sure you implement with most efficient code
<img width="496" height="501" alt="image" src="https://github.com/user-attachments/assets/34ecf132-4889-4eb1-8366-2c32df46e114" />


מטרת הציון היא לתת לכל עסקה מספר שמייצג עד כמה היא שונה מנכס ההשוואה שלך. ככל שהציון נמוך יותר, כך העסקה דומה יותר. ציון 0 משמעו התאמה מושלמת.

הציון הסופי ("ציון דמיון") הוא ממוצע משוקלל של ארבעה פרמטרים, שלכל אחד מהם ניתן "ציון עונשין" בין 0 ל-100 (כש-0 הוא התאמה מלאה ו-100 הוא שוני מקסימלי).

הנה ארבעת הפרמטרים והמשקל של כל אחד מהם בציון הסופי:

שטח (40% מהציון):

לוגיקה: חישוב ההבדל באחוזים בין שטח העסקה לשטח נכס ההשוואה.

חישוב: ההפרש באחוזים מוכפל ב-200. המשמעות היא שהבדל של 50% (או יותר) בשטח ייתן את העונש המקסימלי (100 נקודות).

דוגמה: אם הנכס שלך הוא 100 מ"ר ועסקה היא 110 מ"ר (10% הבדל), ציון השטח יהיה 20.

שנת בניה (20% מהציון):

לוגיקה: חישוב ההבדל בשנים.

חישוב: כל שנת הפרש שווה 5 נקודות עונשין. הציון מוגבל למקסימום 100.

דוגמה: אם הנכס שלך מ-1970 ועסקה מ-1975 (5 שנים הבדל), ציון שנת הבניה יהיה 25.

קומה (20% מהציון):

לוגיקה: חישוב ההבדל במספר הקומות (הקוד יודע לטפל ב-'ק' בתור קומה 0).

חישוב: כל קומת הפרש שווה 25 נקודות עונשין. הציון מוגבל למקסימום 100.

דוגמה: אם הנכס שלך בקומה 2 ועסקה בקומה 0 ('ק'), ההבדל הוא 2 קומות, וציון הקומה יהיה 50.

חניה (20% מהציון):

לוגיקה: בדיקה בינארית (כן/לא).

חישוב: אם לנכס אחד יש חניה (כלומר, ערך גדול מ-0) ולשני אין (ערך 0), הציון הוא 100 (עונש מקסימלי). אם לשניהם יש חניה, או שלשניהם אין חניה, הציון הוא 0.

חישוב הציון הסופי
הציון הסופי שאתה רואה בעמודה החדשה הוא פשוט ממוצע משוקלל של ארבעת ציוני העונשין האלה:

(ציון שטח * 0.4) + (ציון שנת בניה * 0.2) + (ציון קומה * 0.2) + (ציון חניה * 0.2)

זו הסיבה שככל שהציון הסופי נמוך יותר, כך העסקה נחשבת רלוונטית ודומה יותר לנכס ההשוואה שלך.
