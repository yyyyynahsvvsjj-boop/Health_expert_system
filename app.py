import streamlit as str_ui

# إعدادات الصفحة الاحترافية
str_ui.set_page_config(
    page_title="Medical Prescription & Expert System",
    page_icon="🩺",
    layout="centered"
)

# القواميس الشاملة للغات
translations = {
    "English": {
        "title": "🩺 Clinical Expert System & Electronic Prescription",
        "subtitle": "Official Medical Report & Tailored Patient Care Plan",
        "step1": "1. Patient Vital Statistics & Activity",
        "age": "Age (Years)",
        "weight": "Weight (kg)",
        "height": "Height (cm)",
        "activity": "Activity Level",
        "activities": [
            "Sedentary / Desk Job (Minimal movement)",
            "Lightly Active (Light exercise 1-2 days/week)",
            "Moderately Active (Exercise 3-5 days/week)",
            "Very Active (Intense exercise 6-7 days/week)",
            "Professional Athlete (Daily heavy training)",
            "Low Mobility / Senior (Light daily walking)"
        ],
        "step2": "2. Clinical History, Acute Symptoms & Goals",
        "chronic_label": "Chronic Medical Conditions (Select all that apply):",
        "chronic_options": ["Diabetes", "Hypertension", "Knee Osteoarthritis", "High Cholesterol"],
        "acute_label": "Current Acute Symptoms / Complaints:",
        "acute_options": ["Headache / Migraine", "Common Cold & Flu", "Cough & Sore Throat", "Eye Inflammation / Conjunctivitis"],
        "goal_label": "Primary Health Goal:",
        "goal_options": [
            "Weight Loss & Fat Burning (Cutting)",
            "Maintain Current Weight & Balance",
            "Weight Gain & Muscle Building (Bulking)",
            "Symptom Recovery & Management",
            "Boost Immunity & Daily Energy",
            "Blood Sugar & Pressure Control",
            "Joint Health & Mobility Support"
        ],
        "btn_run": "Issue Official Medical Prescription & Report",
        "report_header": "📋 OFFICIAL MEDICAL PRESCRIPTION & CLINICAL REPORT",
        "patient_info": "Patient Clinical Summary",
        "rx_title": "Rx - Medical Treatment & Directives",
        "diet_title": "🍽️ Daily Meal Plan & Nutritional Table",
        "fit_title": "🏃 Physical Activity & Lifestyle Plan",
        "gold_rules": "⭐ Golden Rules for Fast Results"
    },
    "العربية": {
        "title": "🩺 النظام الخبير الطبي وإصدار الروشتات الإلكترونية",
        "subtitle": "تقرير طبي معتمد وخطة علاجية وتغذوية مخصصة للمريض",
        "step1": "الخطوة الأولى: القياسات الحيوية ونمط النشاط اليومي",
        "age": "العمر (بالسنوات)",
        "weight": "الوزن (كجم)",
        "height": "الطول (سم)",
        "activity": "مستوى النشاط اليومي (اختر الأنسب)",
        "activities": [
            "قليل جداً / عمل مكتبي (حركة محدودة جداً)",
            "نشاط خفيف (تمرين خفيف 1-2 أيام أسبوعياً)",
            "نشاط معتدل (تمرين 3-5 أيام أسبوعياً)",
            "نشاط عالي (تمرين شاق 6-7 أيام أسبوعياً)",
            "رياضي محترف (تدريبات يومية مكثفة)",
            "حركة محدودة / كبار السن (مشي خفيف يومي)"
        ],
        "step2": "الخطوة الثانية: التاريخ المرضي، الأعراض الحالية، والأهداف",
        "chronic_label": "الأمراض المزمنة (إن وجدت - اختر الكل المناسب):",
        "chronic_options": ["مرض السكر", "ارتفاع ضغط الدم", "خشونة الركبة والمفاصل", "ارتفاع الكوليسترول"],
        "acute_label": "الأعراض الحادة الحالية (التي يشكو منها المريض الآن):",
        "acute_options": ["الصداع / الصداع النصفي", "نزلات البرد والإنفلونزا", "الكحة والتهاب الحلق", "التهاب العين والاحمرار"],
        "goal_label": "الهدف العلاجي والصحي الأساسي:",
        "goal_options": [
            "خسارة الوزن وزيادة الحرق (تنشيف / خسارة دهون)",
            "الحفاظ على الوزن الحالي وثباته",
            "زيادة الوزن وبناء العضلات (تضخيم / زيادة الكتلة)",
            "التعافي السريع وإدارة الأعراض",
            "رفع المناعة والطاقة اليومية",
            "ضبط مستويات السكر والضغط بانتظام",
            "دعم صحة المفاصل وتقليل الآلام"
        ],
        "btn_run": "إصدار الروشتة الطبية والتقرير الإكلينيكي الشامل",
        "report_header": "📋 روشتة طبية معتمدة وتقرير إكلينيكي مفصل",
        "patient_info": "ملخص الفحص السريري للمريض",
        "rx_title": "Rx - العلاج الدوائي والإرشادات الطبية المباشرة",
        "diet_title": "🍽️ جدول الوجبات اليومية والنظام الغذائي",
        "fit_title": "🏃 خطة النشاط البدني والحياة اليومية",
        "gold_rules": "⭐ القواعد الذهبية لسرعة النتائج"
    }
}

# شريط اختيار اللغة
str_ui.sidebar.title("Settings / الإعدادات")
lang = str_ui.sidebar.selectbox("Language / اللغة", ["العربية", "English"])
t = translations[lang]

# العنوان الرئيسي
str_ui.title(t["title"])
str_ui.markdown(t["subtitle"])
str_ui.divider()

# نموذج الإدخال
with str_ui.form("prescription_form"):
    str_ui.subheader(t["step1"])
    col1, col2, col3 = str_ui.columns(3)
    with col1:
        age = str_ui.number_input(t["age"], min_value=10, max_value=100, value=28)
    with col2:
        weight = str_ui.number_input(t["weight"], min_value=30.0, max_value=200.0, value=75.0)
    with col3:
        height = str_ui.number_input(t["height"], min_value=100.0, max_value=220.0, value=170.0)
        
    activity_level = str_ui.selectbox(t["activity"], t["activities"])

    str_ui.subheader(t["step2"])
    selected_chronic = str_ui.multiselect(t["chronic_label"], t["chronic_options"])
    selected_acute = str_ui.multiselect(t["acute_label"], t["acute_options"])
    health_goal = str_ui.selectbox(t["goal_label"], t["goal_options"])

    submitted = str_ui.form_submit_button(t["btn_run"])

# قاعدة المعرفة الطبية والروشتات الاحترافية
medical_knowledge = {
    "مرض السكر": {
        "rx": "1. منظم السكر الموصوف (مثل ميتفورمين) بانتظام بعد الأكل.\n2. قياس السكر صائم وفاطر بصفة دورية.\n3. الاحتفاظ بمصدر سكريات سريع تحسباً لأي هبوط مفاجئ.",
        "fit": "المشي المنتظم لمدة 30 إلى 45 دقيقة يومياً."
    },
    "Diabetes": {
        "rx": "1. Prescribed oral hypoglycemic agents regularly after meals.\n2. Regular blood glucose monitoring.\n3. Keep fast-acting glucose sources nearby.",
        "fit": "Brisk walking for 30-45 minutes daily."
    },
    "ارتفاع ضغط الدم": {
        "rx": "1. الالتزام بأدوية خفض ضغط الدم في موعدها الثابت.\n2. قياس الضغط يومياً وتدوين القراءات.\n3. تجنب الانفعالات العصبية.",
        "fit": "المشي الهادئ، تمارين التنفس العميق والاسترخاء."
    },
    "Hypertension": {
        "rx": "1. Strict adherence to prescribed antihypertensive medications.\n2. Daily blood pressure logging.\n3. Stress management.",
        "fit": "Calm walking, deep breathing exercises."
    },
    "خشونة الركبة والمفاصل": {
        "rx": "1. جل موضعي مسكن ومضاد للالتهاب عند الأزمات.\n2. مكملات غذائية لصحة الغضاريف (أوميغا 3).\n3. تجنب الجلوس الخاطئ على الأرض.",
        "fit": "السباحة، تمارين تقوية عضلات الساقين بدون تحميل على المفصل."
    },
    "Knee Osteoarthritis": {
        "rx": "1. Topical anti-inflammatory gel during pain flare-ups.\n2. Joint health supplements (Omega-3).\n3. Avoid prolonged sitting on the floor.",
        "fit": "Swimming, seated leg strengthening exercises."
    },
    "ارتفاع الكوليسترول": {
        "rx": "1. أدوية خفض الدهون (الستاتينات) إن وصفها الطبيب.\n2. إجراء تحليل دهون شامل كل 3 إلى 6 أشهر.",
        "fit": "تمارين كارديو منتظمة (جري خفيف، مشي سريع، سباحة)."
    },
    "High Cholesterol": {
        "rx": "1. Statin therapy as prescribed.\n2. Periodic lipid profile testing.",
        "fit": "Regular cardio exercises (jogging, brisk walking)."
    },
    "الصداع / الصداع النصفي": {
        "rx": "1. مسكن آلام بسيط (باراسيتامول) عند حدوث النوبة.\n2. الجلوس في غرفة مظلمة وهادئة تماماً.\n3. شرب كميات وافرة من الماء.",
        "fit": "إراحة الجسم تماماً أثناء النوبة، مع إطالة خفيفة للرقبة والكتفين بعدها."
    },
    "Headache / Migraine": {
        "rx": "1. Over-the-counter mild analgesic (Paracetamol).\n2. Rest in a dark, quiet room.\n3. Adequate hydration.",
        "fit": "Complete physical rest during attacks."
    },
    "نزلات البرد والإنفلونزا": {
        "rx": "1. خافض حرارة ومسكن (باراسيتامول).\n2. مضادات احتقان للأنف وقطرات محلول ملحي.\n3. فيتامين سي وراحة تامّة.",
        "fit": "راحة تامة في السرير وعدم ممارسة أي مجهود بدني."
    },
    "Common Cold & Flu": {
        "rx": "1. Antipyretic and analgesic (Paracetamol).\n2. Nasal decongestants.\n3. Vitamin C and bed rest.",
        "fit": "Absolute bed rest with zero physical exertion."
    },
    "الكحة والتهاب الحلق": {
        "rx": "1. شراب مهدئ للسعال أو موسع للشعب الهوائية.\n2. أقراص استحلاب ملطفة للحلق.\n3. الغرغرة بالماء الدافئ والملح.",
        "fit": "الراحة الصوتية والبدنية، وتجنب الهواء البارد والأتربة."
    },
    "Cough & Sore Throat": {
        "rx": "1. Appropriate cough syrup.\n2. Soothing throat lozenges.\n3. Warm saltwater gargles.",
        "fit": "Vocal and physical rest."
    },
    "التهاب العين والاحمرار": {
        "rx": "1. قطرات عيون مرطبة أو مضادة للحساسية/الالتهاب.\n2. كمادات باردة أو دافئة نظيفة.\n3. تجنب فرك العين نهائياً وغسل اليدين.",
        "fit": "إراحة العين تماماً من الشاشات، وارتداء نظارة شمسية."
    },
    "Eye Inflammation / Conjunctivitis": {
        "rx": "1. Prescribed lubricating or anti-inflammatory eye drops.\n2. Clean compresses.\n3. Strictly avoid rubbing the eyes.",
        "fit": "Complete screen rest for the eyes."
    }
}

# عند الضغط على زر التشغيل
if submitted:
    h_m = height / 100.0
    bmi = weight / (h_m ** 2)
    
    if bmi < 18.5:
        bmi_status = "Underweight / نحيف"
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal Weight / وزن مثالي وطبيعي"
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight / زيادة في الوزن"
    else:
        bmi_status = "Obese / سمنة مفرطة"

    str_ui.success(t["report_header"])
    
    str_ui.markdown(f"### 🏥 {t['patient_info']}")
    c1, c2, c3 = str_ui.columns(3)
    c1.metric(label="BMI", value=f"{bmi:.2f}")
    c2.write(f"**العمر / Age:** {age} سنة")
    c3.write(f"**الوزن / الطول:** {weight}كغ / {height}سم")
    
    str_ui.info(f"📌 **التصنيف الصحي:** {bmi_status} \n\n🎯 **الهدف العلاجي المختار:** {health_goal} | ⚡ **النشاط:** {activity_level}")

    str_ui.divider()

    all_selected = selected_chronic + selected_acute

    if not all_selected:
        str_ui.warning("⚠️ لم يتم تحديد أي أمراض أو أعراض. إليك الروشتة والتوجيهات العامة:")
        all_selected = ["التوجيهات العامة"]
        medical_knowledge["التوجيهات العامة"] = {
            "rx": "1. لا توجد أدوية مطلوبة حالياً.\n2. الفحص الدوري الروتيني وشرب الماء بانتظام.",
            "fit": "المشي اليومي لمدة 30 دقيقة للحفاظ على اللياقة."
        }

    for item in all_selected:
        rec = medical_knowledge.get(item, {
            "rx": "استشر الطبيب المختص لتحديد العلاج المناسب.",
            "fit": "ممارسة النشاط البدني الخفيف المنتظم."
        })
        
        with str_ui.expander(f"🩺 روشتة وتقرير حالة: **{item}**", expanded=True):
            
            str_ui.markdown(f"#### {t['rx_title']}")
            str_ui.code(rec["rx"], language=None)
            
            # جدول الأكل الاحترافي المطابق تماماً للصورة الجديدة
            str_ui.markdown(f"#### {t['diet_title']}")
            
            # التحقق من هدف المريض لتغيير جدول الأكل (تنشيف vs تضخيم)
            is_bulking = "زيادة الوزن" in health_goal or "Bulking" in health_goal
            
            if lang == "العربية":
                if is_bulking:
                    table_markdown = """
| الوجبة | الخيار الأول | الخيار الثاني | الخيار الثالث | ملاحظات هامة |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **الإفطار** | 4 بيضات مسلوقة + كوب حليب كامل الدسم + 3 تمرات + رغيف بلدي | طبق فول كبير بزيت الزيتون والبطاطس المسلوقة + رغيف بلدي + جبنة قريش | فطير مشلتت خفيف أو توست أبيض مع عبد وطحينة + كوب حليب | طاقة عالية لزيادة الوزن وبناء العضلات |
| 🍗 **الغداء** | 200 جم لحم أو دجاج مشوي + طبق أرز كبير (8 ملاعق) + خضار بالصلصة + بطاطس پيوريه | صينية مكرونة بشاميل أو رقاق باللحمة المفرومة + سلطة خضراء + قطعة لحم | سمك مقلي أو مشوي بزيت ذرة + أرز صيادية كبير + سلطة | سعرات حرارية مرتفعة ومناسبة للتضخيم |
| 🥗 **العشاء** | علبة تونة كاملة + طبق مكرونة مسلوقة + عصير مانجو أو جوافة طبيعي | عريكة أو شوفان بالحليب والعسل والمكسرات وزبدة الفول السوداني | سندوتشات جبنة رومي أو أبيض كامل الدسم + بيض مقلي بالزبدة | وجبة غنية قبل النوم لزيادة الكتلة |
"""
                else:
                    table_markdown = """
| الوجبة | الخيار الأول | الخيار الثاني | الخيار الثالث | ملاحظات هامة |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **الإفطار** | 3 بيضات مستوية أو مقلية بمعلقة زيت زيتون + ربع رغيف بلدي + خيار وجرجير | 4 ملاعق فول بزيت زيتون وكمون + ربع رغيف بلدي + بيضة مسلوقة أو قطعة جبنة قريش | عجة بيض بالخضروات وفلفل رومي + ربع رغيف بلدي | بداية نشطة ومشبع لفترة طويلة |
| 🍗 **الغداء** | 150-200 جم صدور فراخ مشوية أو مسلوقة أو لحم مفروم قليل الدهن + 5 ملاعق أرز أو مكرونة + طبق خضار سوتيه + سلطة خضيرة | 2 سمكة مشوية + ربع رغيف بلدي كامل أو 5 ملاعق أرز + طبق سلطة خضراء كبير | بروتين (علبة تونة مصفاة من الزيت) + نشويات (رغيف بلدي كامل أو 5 ملاعق مكرونة) + خضار (طبق خضار سوتيه + سلطة) | معلقة زيت زيتون وليمون فقط على السلطة |
| 🥗 **العشاء** | 150 جم جبنة قريش بالطماطم والخيار ورشة زعتر + ربع رغيف بلدي | علبة تونة مصفاة تماماً + طبق سلطة خضراء | كوب زبادي يوناني (أو عادي) + نص معلقة عسل نحل + معلقة بدر كتان أو شيا | وجبة خفيفة ومناسبة قبل النوم |
"""
            else:
                table_markdown = """
| Meal | Option 1 | Option 2 | Option 3 | Important Notes |
| :--- | :--- | :--- | :--- | :--- |
| 🍳 **Breakfast** | 3 fried/boiled eggs with olive oil + quarter bread + cucumber & arugula | 4 spoons fava beans with olive oil + quarter bread + egg or cottage cheese | Vegetable egg omelet with quarter bread | Active start, long satiety |
| 🍗 **Lunch** | 150-200g grilled chicken/lean meat + 5 spoons rice/pasta + sautéed veggies + salad | 2 grilled fish + quarter bread or 5 spoons rice + large green salad | Tuna (drained) + whole bread or pasta + vegetable soup + salad | Only olive oil and lemon on salad |
| 🥗 **Dinner** | 150g cottage cheese with tomatoes, cucumber, thyme + quarter bread | Drained canned tuna + green salad | Greek/regular yogurt + half spoon honey + flax/chia seeds | Light meal suitable before bed |
"""
            str_ui.markdown(table_markdown)
            
            str_ui.markdown(f"#### {t['fit_title']}")
            str_ui.write(f"🚶 {rec['fit']}")
            
        str_ui.write("")

    # القواعد الذهبية لسرعة النتائج (مطابقة للصورة تماماً)
    str_ui.info(f"""
### {t['gold_rules']}
💧 **شرب المياه:** من 2.5 إلى 3 لتراً يومياً لزيادة معدل الحرق ومنع الإحساس الوهمي بالجوع.  
🚶 **الحركة الخفيفة:** المشي 15-20 دقيقة في منتصف اليوم أو بعد الغداء لتعويض الجلوس المكتبي.  
🚫 **السكر والمشروبات:** استبدال السكر الأبيض بسكر دايت ومنع العصائر المعلبة تماماً.
    """)

    str_ui.success("✨ تم إصدار هذه الروشتة والتقرير الإكلينيكي إلكترونياً بنجاح.")
