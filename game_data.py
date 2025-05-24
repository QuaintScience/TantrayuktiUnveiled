"""
Game data for Tantrayukti educational game
Enhanced content with more fragments and detailed descriptions
"""

TANTRAYUKTI_DEVICES = {
    "Prayojana": {
        "name": "Prayojana",
        "description": "Stating the objective or purpose of the treatise",
        "detailed_desc": "The fundamental principle that establishes why a text exists and what it aims to accomplish. Like a lamp that illuminates the path ahead.",
        "category": "Purpose & Intent",
        "sanskrit": "प्रयोजन"
    },
    "Adhikarana": {
        "name": "Adhikaraṇa", 
        "description": "Anchoring the central topic or theme",
        "detailed_desc": "The compass that determines the main subject matter, ensuring the discourse remains focused on its core theme without deviation.",
        "category": "Structure & Focus",
        "sanskrit": "अधिकरण"
    },
    "Uddesa": {
        "name": "Uddeśa",
        "description": "Providing a brief overview or listing of subjects",
        "detailed_desc": "Like the table of contents of ancient wisdom, presenting a systematic preview of topics to be explored in detail.",
        "category": "Organization",
        "sanskrit": "उद्देश"
    },
    "Nirdesa": {
        "name": "Nirdeśa",
        "description": "Offering detailed explanation of subjects previously listed",
        "detailed_desc": "The detailed exposition that follows the overview, like a master craftsman explaining each intricate detail of their art.",
        "category": "Elaboration",
        "sanskrit": "निर्देश"
    },
    "Uhya": {
        "name": "Ūhya",
        "description": "Inferring or deducing meaning from context",
        "detailed_desc": "The art of reading between the lines, understanding implicit meanings through contextual reasoning - the scholar's intuitive wisdom.",
        "category": "Inference & Reasoning",
        "sanskrit": "ऊह्य"
    },
    "Drstanta": {
        "name": "Dr̥ṣṭānta",
        "description": "Using illustrative analogies to clarify concepts",
        "detailed_desc": "Making the abstract tangible through familiar comparisons, like explaining the wind through the movement of leaves.",
        "category": "Clarification",
        "sanskrit": "दृष्टान्त"
    },
    "Purvapaksa": {
        "name": "Pūrvapakṣa",
        "description": "Presenting preliminary objections or opposing views",
        "detailed_desc": "The initial challenge in philosophical discourse, setting up arguments that will be examined and refined through debate.",
        "category": "Dialectical Reasoning",
        "sanskrit": "पूर्वपक्ष"
    },
    "Uttarapaksa": {
        "name": "Uttarapakṣa",
        "description": "Offering conclusive resolution to debates",
        "detailed_desc": "The final synthesis that resolves contradictions and establishes the ultimate truth after thorough examination.",
        "category": "Dialectical Reasoning", 
        "sanskrit": "उत्तरपक्ष"
    },
    "Apavarga": {
        "name": "Apavarga",
        "description": "Introducing exceptions to general rules",
        "detailed_desc": "Recognizing that wisdom includes knowing when rules don't apply - the nuanced understanding of contextual boundaries.",
        "category": "Precision & Exceptions",
        "sanskrit": "अपवर्ग"
    },
    "Vidhana": {
        "name": "Vidhāna",
        "description": "Organizing thematic arrangement in logical sequence",
        "detailed_desc": "The architectural principle of knowledge organization, arranging ideas in their most natural and comprehensible order.",
        "category": "Structure & Organization",
        "sanskrit": "विधान"
    },
    "Viparyaya": {
        "name": "Viparyaya",
        "description": "Warning against inversions or common errors",
        "detailed_desc": "The cautionary voice that prevents misunderstanding by highlighting where confusion typically arises.",
        "category": "Error Prevention",
        "sanskrit": "विपर्यय"
    },
    "Svasamjna": {
        "name": "Svasaṁjñā",
        "description": "Defining and standardizing technical terminology",
        "detailed_desc": "Establishing precise meanings for specialized terms, creating a shared vocabulary for scholarly discourse.",
        "category": "Precision & Definition",
        "sanskrit": "स्वसंज्ञा"
    },
    "Atidesa": {
        "name": "Atideśa",
        "description": "Extending principles from one context to another",
        "detailed_desc": "The bridge-building technique that applies established principles to new situations through reasoned extension.",
        "category": "Application & Extension",
        "sanskrit": "अतिदेश"
    },
    "Arthapatti": {
        "name": "Arthāpatti",
        "description": "Logical implication or presumption",
        "detailed_desc": "The reasoning that reveals what must be true based on what is observed, like deducing fire from smoke.",
        "category": "Logical Reasoning",
        "sanskrit": "अर्थापत्ति"
    }
}

TEXTUAL_FRAGMENTS = [
    {
        "id": "legal_01",
        "text": "This treatise aims to establish the principles of righteous governance and the duties of rulers in maintaining dharma across the kingdom.",
        "correct_yukti": ["Prayojana"],
        "discipline": "Legal/Governance",
        "purpose": "Establishing the fundamental purpose of political treatise",
        "source": "Arthaśāstra tradition",
        "difficulty": "beginner",
        "explanation": "This clearly states the overall objective and purpose of the entire work."
    },
    {
        "id": "medical_01", 
        "text": "Though the patient exhibits fever and fatigue, the texts describe neither this combination nor its treatment. The physician must deduce the underlying dośa imbalance from these manifest symptoms.",
        "correct_yukti": ["Uhya"],
        "discipline": "Medical/Diagnostic",
        "purpose": "Contextual inference in medical diagnosis",
        "source": "Caraka Saṃhitā tradition",
        "difficulty": "intermediate",
        "explanation": "Medical diagnosis often requires inferring hidden causes from visible symptoms."
    },
    {
        "id": "philosophy_01",
        "text": "The initial position argues: 'Sound is impermanent because it is produced and destroyed, like a clay pot.' This view shall now be examined.",
        "correct_yukti": ["Purvapaksa"],
        "discipline": "Philosophy/Debate", 
        "purpose": "Presenting the opening argument in philosophical dialectic",
        "source": "Nyāya-Vaiśeṣika tradition",
        "difficulty": "intermediate",
        "explanation": "This establishes the initial position that will be debated and potentially refuted."
    },
    {
        "id": "grammar_01",
        "text": "The six primary categories of existence are: substance (dravya), quality (guṇa), action (karma), universal (sāmānya), particular (viśeṣa), and inherence (samavāya). Each will be examined in the following sections.",
        "correct_yukti": ["Uddesa"],
        "discipline": "Philosophy/Systematic",
        "purpose": "Providing systematic overview of topics to be covered",
        "source": "Vaiśeṣika Darśana",
        "difficulty": "beginner",
        "explanation": "This gives a comprehensive preview of the main topics without detailed explanation."
    },
    {
        "id": "medical_02",
        "text": "Substance (dravya) is defined as the substratum of qualities and actions. It neither inheres in anything else nor depends on other substances for its existence. The nine substances are: earth, water, fire, air, ether, time, space, self, and mind.",
        "correct_yukti": ["Nirdesa"],
        "discipline": "Philosophy/Medical",
        "purpose": "Detailed explanation following previous overview",
        "source": "Vaiśeṣika-Caraka synthesis",
        "difficulty": "intermediate", 
        "explanation": "This provides the detailed exposition of 'dravya' that was mentioned in the earlier overview."
    },
    {
        "id": "legal_02",
        "text": "A well-administered kingdom is like a perfectly balanced chariot - if any single component fails, whether wheel or axle, the entire vehicle becomes useless, no matter how fine the other parts.",
        "correct_yukti": ["Drstanta"],
        "discipline": "Legal/Governance",
        "purpose": "Illustrative analogy for administrative principle",
        "source": "Arthaśāstra tradition",
        "difficulty": "beginner",
        "explanation": "The chariot analogy makes the abstract concept of administrative interdependence concrete and memorable."
    },
    {
        "id": "philosophy_02",
        "text": "Having examined the preliminary objection, we now establish the final position: Sound possesses permanence in its essential nature as linguistic category, though its audible manifestation is indeed transitory.",
        "correct_yukti": ["Uttarapaksa"],
        "discipline": "Philosophy/Debate", 
        "purpose": "Conclusive resolution of philosophical debate",
        "source": "Vyākaraṇa-Nyāya synthesis",
        "difficulty": "advanced",
        "explanation": "This provides the final philosophical resolution after examining and refining the initial arguments."
    },
    {
        "id": "medical_03",
        "text": "All dietary prescriptions apply universally, EXCEPT when the patient's constitution (prakr̥ti) indicates a predominant doṣa that contradicts the general recommendation.",
        "correct_yukti": ["Apavarga"],
        "discipline": "Medical/Therapeutic",
        "purpose": "Specifying exceptions to general medical rules",
        "source": "Caraka Saṃhitā",
        "difficulty": "intermediate",
        "explanation": "Medical treatment recognizes that individual constitution may require exceptions to general dietary guidelines."
    },
    {
        "id": "grammar_02",
        "text": "In this discourse, the term 'dhātu' refers exclusively to the eighteen bodily constituents responsible for physiological functions, not to the verbal roots of grammatical analysis.",
        "correct_yukti": ["Svasamjna"],
        "discipline": "Medical/Technical",
        "purpose": "Defining technical terminology to avoid confusion",
        "source": "Suśruta Saṃhitā",
        "difficulty": "beginner",
        "explanation": "This establishes a precise technical definition to prevent confusion with the grammatical meaning of 'dhātu'."
    },
    {
        "id": "philosophy_03",
        "text": "Beware: Confusing the sequence of logical reasoning can lead to the error of taking effect for cause, like mistaking the lamp's shadow for its light.",
        "correct_yukti": ["Viparyaya"],
        "discipline": "Philosophy/Logic",
        "purpose": "Warning against common logical errors",
        "source": "Nyāya Darśana",
        "difficulty": "intermediate",
        "explanation": "This cautions against a specific type of logical inversion that commonly occurs in reasoning."
    },
    {
        "id": "legal_03",
        "text": "The principles of justice established for resolving disputes between merchants shall be extended, with appropriate modifications, to conflicts arising between artisan guilds.",
        "correct_yukti": ["Atidesa"],
        "discipline": "Legal/Judicial",
        "purpose": "Extending legal principles to new contexts",
        "source": "Dharmaśāstra tradition",
        "difficulty": "advanced",
        "explanation": "This demonstrates how established legal principles can be thoughtfully applied to similar but distinct situations."
    },
    {
        "id": "medical_04",
        "text": "Since the patient consumed only cooling foods yet developed heat-related symptoms, there must be an internal fire-generating factor not mentioned in the dietary history.",
        "correct_yukti": ["Arthapatti"],
        "discipline": "Medical/Diagnostic",
        "purpose": "Logical implication in medical reasoning",
        "source": "Caraka Saṃhitā",
        "difficulty": "advanced",
        "explanation": "The physician uses logical implication to deduce hidden causal factors from apparent contradictions."
    },
    {
        "id": "ritual_01",
        "text": "The fire ceremony shall be conducted at dawn. The offerings consist of clarified butter, sacred grains, and aromatic herbs. The mantras to be recited are those specified in the Ṛgveda, chapters 1 through 3.",
        "correct_yukti": ["Vidhana"],
        "discipline": "Ritual/Religious",
        "purpose": "Systematic arrangement of ritual procedures",
        "source": "Kalpa Sūtra tradition",
        "difficulty": "beginner",
        "explanation": "This organizes ritual elements in their proper sequential and thematic order."
    },
    {
        "id": "philosophy_04",
        "text": "Now, focusing our inquiry on the nature of consciousness, we shall examine whether awareness can exist independently of mental modifications.",
        "correct_yukti": ["Adhikarana"],
        "discipline": "Philosophy/Metaphysics",
        "purpose": "Establishing the central topic of philosophical investigation",
        "source": "Yoga Darśana",
        "difficulty": "intermediate",
        "explanation": "This anchors the discourse on a specific philosophical topic and maintains focus on that central theme."
    },
    {
        "id": "astronomy_01",
        "text": "Just as a skilled navigator reads the stars to determine direction across trackless waters, so must the astrologer interpret planetary positions to understand their influence on human affairs.",
        "correct_yukti": ["Drstanta"],
        "discipline": "Astronomy/Astrology",
        "purpose": "Analogical explanation of astrological reasoning",
        "source": "Jyotiśa tradition",
        "difficulty": "beginner",
        "explanation": "The navigator analogy helps explain the interpretive nature of astrological practice."
    }
]

# Organize fragments by difficulty for progressive learning
FRAGMENTS_BY_DIFFICULTY = {
    "beginner": [f for f in TEXTUAL_FRAGMENTS if f["difficulty"] == "beginner"],
    "intermediate": [f for f in TEXTUAL_FRAGMENTS if f["difficulty"] == "intermediate"], 
    "advanced": [f for f in TEXTUAL_FRAGMENTS if f["difficulty"] == "advanced"]
}

# Organize by discipline for focused study
FRAGMENTS_BY_DISCIPLINE = {}
for fragment in TEXTUAL_FRAGMENTS:
    discipline = fragment["discipline"]
    if discipline not in FRAGMENTS_BY_DISCIPLINE:
        FRAGMENTS_BY_DISCIPLINE[discipline] = []
    FRAGMENTS_BY_DISCIPLINE[discipline].append(fragment)
