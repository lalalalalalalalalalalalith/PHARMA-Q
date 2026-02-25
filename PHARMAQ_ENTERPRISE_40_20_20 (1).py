
import streamlit as st

st.set_page_config(page_title="PHARMAQ", layout="wide")

# ------------------ UI Styling ------------------
st.markdown("""
<style>
.big-title {font-size: 42px; font-weight: 700; color: white;}
.module-btn {border-radius: 12px; padding: 8px;}
.footer-box {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    margin-top: 30px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">PHARMAQ</div>', unsafe_allow_html=True)
st.markdown("### Clinical Decision Support System")

st.divider()

module = st.radio(
    "Select Module",
    ["Symptom to OTC", "Drug Interaction Checker", "Food-Drug Interaction Checker"],
    horizontal=True
)

st.divider()

# ======================================================
# 1️⃣ SYMPTOM TO OTC 
# ======================================================

if module == "Symptom to OTC":

    symptom_db = {
        "fever": "Paracetamol 500-650mg q6-8h (max 4g/day). Consult if >3 days or >103°F.",
        "cold": "Cetirizine 10mg OD. Steam inhalation. Consult if sinus pain.",
        "cough": "Dextromethorphan 10-20mg q6h. Consult if blood in sputum.",
        "headache": "Paracetamol 500mg / Ibuprofen 400mg.",
        "acidity": "Pantoprazole 40mg before food.",
        "diarrhea": "ORS + Zinc 20mg daily.",
        "vomiting": "Ondansetron 4mg.",
        "allergy": "Levocetirizine 5mg OD.",
        "back pain": "Ibuprofen 400mg + topical NSAID.",
        "eye redness": "Lubricant eye drops.",
        "constipation": "Isabgol husk 1-2 tsp at night.",
        "sore throat": "Warm saline gargle + Lozenges.",
        "toothache": "Ibuprofen 400mg. Dental consult required.",
        "gas": "Simethicone 80mg.",
        "menstrual pain": "Mefenamic acid 500mg.",
        "migraine": "Sumatriptan 50mg.",
        "skin rash": "Calamine lotion.",
        "itching": "Cetirizine 10mg.",
        "insomnia": "Melatonin 3mg.",
        "anxiety mild": "Non-pharma relaxation techniques.",
        "muscle pain": "Diclofenac gel.",
        "ear pain": "Analgesic + ENT review if persists.",
        "burn minor": "Silver sulfadiazine cream.",
        "dehydration": "ORS solution.",
        "nausea": "Domperidone 10mg.",
        "indigestion": "Antacid syrup 10ml.",
        "hemorrhoids": "Topical hydrocortisone cream.",
        "joint pain": "NSAIDs short term.",
        "urticaria": "Antihistamine.",
        "acne": "Benzoyl peroxide gel.",
        "dizziness": "Hydration + monitor BP.",
        "high bp mild": "Lifestyle modification + consult.",
        "low bp": "Hydration + salt intake (if safe).",
        "heartburn": "Famotidine 20mg.",
        "sunburn": "Aloe vera gel.",
        "motion sickness": "Dimenhydrinate 50mg.",
        "dry eyes": "Artificial tears.",
        "flu": "Paracetamol + hydration.",
        "sprain": "RICE protocol.",
        "minor cut": "Clean + povidone iodine."
    }

    symptom = st.text_input("Enter symptom")

    if symptom:
        key = symptom.lower().strip()
        if key in symptom_db:
            st.success(symptom_db[key])
        else:
            st.warning("Symptom not found.")

# ======================================================
# 2️⃣ DRUG INTERACTIONS (20)
# ======================================================

elif module == "Drug Interaction Checker":

    interaction_db = {
        ("warfarin","aspirin"): "High bleeding risk.",
        ("warfarin","ibuprofen"): "Increased bleeding.",
        ("sildenafil","nitroglycerin"): "Severe hypotension.",
        ("metformin","contrast"): "Lactic acidosis risk.",
        ("atorvastatin","clarithromycin"): "Myopathy risk.",
        ("paracetamol","alcohol"): "Liver toxicity.",
        ("tramadol","ssri"): "Serotonin syndrome.",
        ("rifampicin","ocp"): "Reduced contraceptive effect.",
        ("amiodarone","warfarin"): "Raised INR.",
        ("digoxin","verapamil"): "Digoxin toxicity.",
        ("lithium","ace inhibitors"): "Lithium toxicity.",
        ("clopidogrel","omeprazole"): "Reduced efficacy.",
        ("ketoconazole","statins"): "Muscle toxicity.",
        ("insulin","beta blockers"): "Mask hypoglycemia.",
        ("benzodiazepine","opioid"): "Respiratory depression.",
        ("methotrexate","nsaid"): "Toxicity risk.",
        ("ssri","mao inhibitor"): "Severe serotonin syndrome.",
        ("ciprofloxacin","theophylline"): "Toxicity risk.",
        ("spironolactone","ace inhibitor"): "Hyperkalemia.",
        ("valproate","lamotrigine"): "Increased lamotrigine toxicity."
    }

    d1 = st.text_input("Drug 1")
    d2 = st.text_input("Drug 2")

    if d1 and d2:
        pair = (d1.lower().strip(), d2.lower().strip())
        rev = (pair[1], pair[0])
        if pair in interaction_db:
            st.error(interaction_db[pair])
        elif rev in interaction_db:
            st.error(interaction_db[rev])
        else:
            st.success("No major interaction in current database.")

# ======================================================
# 3️⃣ FOOD–DRUG INTERACTIONS (20)
# ======================================================

elif module == "Food-Drug Interaction Checker":

    food_db = {
        ("grapefruit","statin"): "Increases statin levels.",
        ("milk","tetracycline"): "Reduced absorption.",
        ("green leafy vegetables","warfarin"): "Reduced anticoagulation.",
        ("alcohol","metronidazole"): "Disulfiram reaction.",
        ("banana","ace inhibitor"): "Hyperkalemia risk.",
        ("coffee","ciprofloxacin"): "Increased caffeine toxicity.",
        ("salt substitute","spironolactone"): "High potassium.",
        ("high protein diet","levodopa"): "Reduced effect.",
        ("cranberry","warfarin"): "Bleeding risk.",
        ("fiber","digoxin"): "Reduced absorption.",
        ("soy","thyroxine"): "Reduced absorption.",
        ("licorice","digoxin"): "Arrhythmia risk.",
        ("alcohol","benzodiazepine"): "Respiratory depression.",
        ("cheese","mao inhibitor"): "Hypertensive crisis.",
        ("ginseng","warfarin"): "Reduced INR control.",
        ("turmeric","anticoagulant"): "Bleeding risk.",
        ("garlic","antiplatelet"): "Bleeding risk.",
        ("fatty meal","griseofulvin"): "Increased absorption.",
        ("caffeine","theophylline"): "Toxicity risk.",
        ("milk","ciprofloxacin"): "Reduced absorption."
    }

    f = st.text_input("Food")
    d = st.text_input("Drug")

    if f and d:
        pair = (f.lower().strip(), d.lower().strip())
        rev = (pair[1], pair[0])
        if pair in food_db:
            st.error(food_db[pair])
        elif rev in food_db:
            st.error(food_db[rev])
        else:
            st.success("No major food-drug interaction found.")

# ------------------ Guidelines Footer ------------------
st.markdown('<div class="footer-box">⚠ GUIDELINES: For educational use only. '
            'Always verify dosing, patient history, pregnancy status, renal/hepatic function. '
            'Refer immediately in emergency symptoms like chest pain, stroke signs, anaphylaxis, severe bleeding.</div>', 
            unsafe_allow_html=True)
