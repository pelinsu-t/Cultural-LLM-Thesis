def chain_of_thought_en(prompt: str) -> str:
    return ("Think through the question step by step before answering. "
            "Identify the cultural concepts being asked about, determine which kinds of norms are "
            "relevant (for example social, workplace, family, or religious norms), "
            "and infer the specific culture or cultural setting the user is referring to. "
            "Then interpret the question within that context and provide a culturally appropriate, "
            "accurate, and context-sensitive answer. \n\n"
            f"{prompt}")

def persona_en(prompt: str, country: str) -> str:
    return(f"Answer as someone who lives in {country} and is familiar with its customs, "
           f"traditions, and everyday norms. Provide responses that reflect how people "
           f"in that culture would typically understand and handle the situation.\n\n"
           f"{prompt}")

def uncertainty_en(prompt:str) -> str:
    return (
        "Before answering, carefully evaluate what can be inferred from the question and what cannot. "
        "Avoid making unsupported assumptions about cultural specifics. When the cultural context is "
        "ambiguous or your confidence is limited, explicitly acknowledge the uncertainty and answer cautiously.\n\n"
        f"{prompt}")

def combined_en(prompt:str, country:str) -> str:
    return ("Reason step by step before answering. Identify the cultural concepts and relevant norms "
            "(e.g., social, workplace, family), and infer the cultural context. "
            f"Answer as a local from {country}, reflecting realistic customs, traditions, and expectations. "
            "Avoid unsupported assumptions. If cultural details are uncertain, acknowledge this and respond cautiously. "
            "Give a clear and culturally appropriate answer.\n\n"
        f"{prompt}")


### GERMAN
def chain_of_thought_de(prompt: str) -> str:
    return ("Denke die Frage Schritt für Schritt durch, bevor du antwortest. "
            "Identifiziere die angesprochenen kulturellen Konzepte, bestimme, welche Arten von Normen "
            "relevant sind (zum Beispiel soziale, berufliche, familiäre oder religiöse Normen), "
            "und erschließe die spezifische Kultur oder den kulturellen Kontext, auf den sich die Anfrage bezieht. "
            "Interpretiere die Frage anschließend innerhalb dieses Kontexts und gib eine kulturell angemessene, "
            "korrekte und kontextsensitive Antwort. \n\n"
            f"{prompt}")

def persona_de(prompt: str, country: str) -> str:
    return (f"Antworte als eine Person, die in {country} lebt und mit den dortigen Bräuchen, "
            f"Traditionen und Alltagsnormen vertraut ist. Gib Antworten, die widerspiegeln, wie Menschen "
            f"in dieser Kultur die Situation typischerweise verstehen und damit umgehen würden.\n\n"
            f"{prompt}")

def uncertainty_de(prompt: str) -> str:
    return (
        "Bevor du antwortest, prüfe sorgfältig, was sich aus der Frage ableiten lässt und was nicht. "
        "Vermeide unbegründete Annahmen über kulturelle Besonderheiten. Wenn der kulturelle Kontext "
        "mehrdeutig ist oder deine Sicherheit begrenzt ist, weise ausdrücklich auf die Unsicherheit hin "
        "und antworte vorsichtig.\n\n"
        f"{prompt}")

def combined_de(prompt: str, country: str) -> str:
    return ("Denke Schritt für Schritt, bevor du antwortest. Identifiziere die kulturellen Konzepte und relevanten Normen "
            "(z. B. soziale, berufliche, familiäre) und erschließe den kulturellen Kontext. "
            f"Antworte als eine lokale Person aus {country} und berücksichtige realistische Bräuche, Traditionen und Erwartungen. "
            "Vermeide unbegründete Annahmen. Wenn kulturelle Details unsicher sind, weise darauf hin und antworte vorsichtig. "
            "Gib eine klare und kulturell angemessene Antwort.\n\n"
            f"{prompt}")


### GREEK
# to be checked
def chain_of_thought_el(prompt: str) -> str:
    return ("Σκέψου την ερώτηση βήμα προς βήμα πριν απαντήσεις. "
        "Εντόπισε τις πολιτισμικές έννοιες που τίθενται, καθόρισε ποια είδη κανόνων είναι "
        "σχετικά (για παράδειγμα κοινωνικοί, επαγγελματικοί, οικογενειακοί ή θρησκευτικοί κανόνες), "
        "και συμπέρανε τον συγκεκριμένο πολιτισμό ή το πολιτισμικό πλαίσιο στο οποίο αναφέρεται ο χρήστης. "
        "Έπειτα ερμήνευσε την ερώτηση μέσα σε αυτό το πλαίσιο και δώσε μια πολιτισμικά κατάλληλη, "
        "ακριβή και ευαίσθητη ως προς το πλαίσιο απάντηση.\n\n"
        f"{prompt}")

def persona_el(prompt: str, country: str) -> str:
    return (f"Απάντησε ως κάποιος που ζει στη {country} και είναι εξοικειωμένος με τα έθιμα, "
            f"τις παραδόσεις και τους καθημερινούς κανόνες της. Παρείχε απαντήσεις που να αντικατοπτρίζουν "
            f"πώς οι άνθρωποι σε αυτήν την κουλτούρα θα κατανοούσαν και θα χειρίζονταν συνήθως την κατάσταση.\n\n"
            f"{prompt}")

def uncertainty_el(prompt: str) -> str:
    return (
        "Πριν απαντήσεις, αξιολόγησε προσεκτικά τι μπορεί να συναχθεί από την ερώτηση και τι όχι. "
        "Απόφυγε να κάνεις ατεκμηρίωτες υποθέσεις σχετικά με πολιτισμικές ιδιαιτερότητες. Όταν το πολιτισμικό πλαίσιο "
        "είναι ασαφές ή η βεβαιότητά σου είναι περιορισμένη, αναγνώρισε ρητά την αβεβαιότητα "
        "και απάντησε με προσοχή.\n\n"
        f"{prompt}")

def combined_el(prompt: str, country: str) -> str:
    return ("Σκέψου βήμα προς βήμα πριν απαντήσεις. Εντόπισε τις πολιτισμικές έννοιες και τους σχετικούς κανόνες "
            "(π.χ. κοινωνικούς, επαγγελματικούς, οικογενειακούς) και συμπέρανε το πολιτισμικό πλαίσιο. "
            f"Απάντησε ως ντόπιος από τη {country}, αντικατοπτρίζοντας ρεαλιστικά έθιμα, παραδόσεις και προσδοκίες. "
            "Απόφυγε ατεκμηρίωτες υποθέσεις. Αν οι πολιτισμικές λεπτομέρειες είναι αβέβαιες, αναγνώρισε το και απάντησε με προσοχή. "
            "Δώσε μια σαφή και πολιτισμικά κατάλληλη απάντηση.\n\n"
            f"{prompt}")


### SPANISH
# to be checked
def chain_of_thought_es(prompt: str) -> str:
    return ("Piensa en la pregunta paso a paso antes de responder. "
            "Identifica los conceptos culturales involucrados, determina qué tipos de normas son "
            "relevantes (por ejemplo, normas sociales, laborales, familiares o religiosas), "
            "e infiere la cultura o el contexto cultural específico al que se refiere el usuario. "
            "Luego, interpreta la pregunta dentro de ese contexto y proporciona una respuesta culturalmente adecuada, "
            "precisa y sensible al contexto.\n\n"
            f"{prompt}")

def persona_es(prompt: str, country: str) -> str:
    return (f"Responde como alguien que vive en {country} y está familiarizado con sus costumbres, "
            f"tradiciones y normas cotidianas. Proporciona respuestas que reflejen cómo las personas "
            f"de esa cultura normalmente entenderían y manejarían la situación.\n\n"
            f"{prompt}")

def uncertainty_es(prompt: str) -> str:
    return (
        "Antes de responder, evalúa cuidadosamente qué se puede inferir de la pregunta y qué no. "
        "Evita hacer suposiciones no fundamentadas sobre aspectos culturales específicos. Cuando el contexto cultural sea "
        "ambiguo o tu nivel de confianza sea limitado, reconoce explícitamente la incertidumbre "
        "y responde con cautela.\n\n"
        f"{prompt}")

def combined_es(prompt: str, country: str) -> str:
    return ("Razona paso a paso antes de responder. Identifica los conceptos culturales y las normas relevantes "
            "(por ejemplo, sociales, laborales o familiares) e infiere el contexto cultural. "
            f"Responde como alguien local de {country}, reflejando costumbres, tradiciones y expectativas realistas. "
            "Evita hacer suposiciones no fundamentadas. Si los detalles culturales son inciertos, reconócelo y responde con cautela. "
            "Da una respuesta clara y culturalmente adecuada.\n\n"
            f"{prompt}")


### ITALIAN
def chain_of_thought_it(prompt: str) -> str:
    return ("Rifletti sulla domanda passo dopo passo prima di rispondere. "
            "Individua i concetti culturali coinvolti, determina quali tipi di norme sono "
            "rilevanti (ad esempio norme sociali, lavorative, familiari o religiose), "
            "e deduci la cultura o il contesto culturale specifico a cui si riferisce l’utente. "
            "Interpreta quindi la domanda all’interno di questo contesto e fornisci una risposta culturalmente appropriata, "
            "accurata e sensibile al contesto.\n\n"
            f"{prompt}")

def persona_it(prompt: str, country: str) -> str:
    return (f"Rispondi come una persona che vive in {country} ed è familiare con le sue usanze, "
            f"tradizioni e norme quotidiane. Fornisci risposte che riflettano come le persone "
            f"in quella cultura comprenderebbero e gestirebbero tipicamente la situazione.\n\n"
            f"{prompt}")

def uncertainty_it(prompt: str) -> str:
    return (
        "Prima di rispondere, valuta attentamente cosa può essere dedotto dalla domanda e cosa no. "
        "Evita di fare supposizioni non supportate su aspetti culturali specifici. Quando il contesto culturale è "
        "ambiguo o il tuo livello di sicurezza è limitato, riconosci esplicitamente l’incertezza "
        "e rispondi con cautela.\n\n"
        f"{prompt}")

def combined_it(prompt: str, country: str) -> str:
    return ("Ragiona passo dopo passo prima di rispondere. Identifica i concetti culturali e le norme rilevanti "
            "(ad esempio sociali, lavorative o familiari) e deduci il contesto culturale. "
            f"Rispondi come una persona locale di {country}, riflettendo usanze, tradizioni e aspettative realistiche. "
            "Evita supposizioni non supportate. Se i dettagli culturali sono incerti, riconoscilo e rispondi con cautela. "
            "Fornisci una risposta chiara e culturalmente appropriata.\n\n"
            f"{prompt}")


### POLISH
# To be checked
def chain_of_thought_pl(prompt: str) -> str:
    return ("Przemyśl pytanie krok po kroku, zanim odpowiesz. "
            "Zidentyfikuj poruszane koncepcje kulturowe, określ, jakie rodzaje norm są "
            "istotne (na przykład normy społeczne, zawodowe, rodzinne lub religijne), "
            "oraz wywnioskuj konkretną kulturę lub kontekst kulturowy, do którego odnosi się użytkownik. "
            "Następnie zinterpretuj pytanie w tym kontekście i udziel odpowiedzi odpowiedniej kulturowo, "
            "dokładnej i uwzględniającej kontekst.\n\n"
            f"{prompt}")

def persona_pl(prompt: str, country: str) -> str:
    return (f"Odpowiadaj jako osoba mieszkająca w {country}, która jest zaznajomiona z jego zwyczajami, "
            f"tradycjami i codziennymi normami. Udzielaj odpowiedzi, które odzwierciedlają, jak ludzie "
            f"w tej kulturze zazwyczaj rozumieją i radzą sobie z daną sytuacją.\n\n"
            f"{prompt}")

def uncertainty_pl(prompt: str) -> str:
    return (
        "Przed udzieleniem odpowiedzi dokładnie oceń, co można wywnioskować z pytania, a czego nie. "
        "Unikaj nieuzasadnionych założeń dotyczących szczegółów kulturowych. Gdy kontekst kulturowy jest "
        "niejednoznaczny lub twoja pewność jest ograniczona, wyraźnie zaznacz niepewność "
        "i odpowiadaj ostrożnie.\n\n"
        f"{prompt}")

def combined_pl(prompt: str, country: str) -> str:
    return ("Rozważaj krok po kroku przed udzieleniem odpowiedzi. Zidentyfikuj koncepcje kulturowe i istotne normy "
            "(np. społeczne, zawodowe, rodzinne) oraz wywnioskuj kontekst kulturowy. "
            f"Odpowiadaj jako osoba lokalna z {country}, odzwierciedlając realistyczne zwyczaje, tradycje i oczekiwania. "
            "Unikaj nieuzasadnionych założeń. Jeśli szczegóły kulturowe są niepewne, zaznacz to i odpowiadaj ostrożnie. "
            "Udziel jasnej i kulturowo odpowiedniej odpowiedzi.\n\n"
            f"{prompt}")


### RUSSIAN
def chain_of_thought_ru(prompt: str) -> str:
    return ("Тщательно продумай вопрос шаг за шагом перед тем, как отвечать. "
            "Определи, какие культурные концепции затрагиваются, установи, какие виды норм являются "
            "релевантными (например, социальные, профессиональные, семейные или религиозные нормы), "
            "и сделай вывод о конкретной культуре или культурном контексте, к которому обращается пользователь. "
            "Затем интерпретируй вопрос в этом контексте и дай культурно уместный, "
            "точный и чувствительный к контексту ответ.\n\n"
            f"{prompt}")

def persona_ru(prompt: str, country: str) -> str:
    return (f"Отвечай как человек, который живёт в {country} и знаком с местными обычаями, "
            f"традициями и повседневными нормами. Давай ответы, отражающие то, как люди "
            f"в этой культуре обычно понимают и справляются с данной ситуацией.\n\n"
            f"{prompt}")

def uncertainty_ru(prompt: str) -> str:
    return (
        "Прежде чем отвечать, внимательно оцени, что можно вывести из вопроса, а что — нет. "
        "Избегай необоснованных предположений о культурных особенностях. Когда культурный контекст "
        "неоднозначен или твоя уверенность ограничена, явно признай неопределённость "
        "и отвечай осторожно.\n\n"
        f"{prompt}")

def combined_ru(prompt: str, country: str) -> str:
    return ("Продумай ответ шаг за шагом перед тем, как отвечать. Определи культурные концепции и соответствующие нормы "
            "(например, социальные, рабочие, семейные) и выведи культурный контекст. "
            f"Отвечай как местный житель из {country}, отражая реалистичные обычаи, традиции и ожидания. "
            "Избегай необоснованных предположений. Если культурные детали неопределённы, признай это и отвечай осторожно. "
            "Дай чёткий и культурно уместный ответ.\n\n"
            f"{prompt}")


### TURKISH
def chain_of_thought_tr(prompt: str) -> str:
    return ("Cevaplamadan önce soruyu adım adım düşün. "
            "Ele alınan kültürel kavramları belirle, hangi tür normlarla "
            "ilgili olduğunu tespit et (örneğin sosyal, işyeri, aile veya dini normlar) "
            "ve kullanıcının atıfta bulunduğu belirli kültürü veya kültürel bağlamı çıkar. "
            "Ardından soruyu bu bağlam içinde yorumla ve kültürel olarak uygun, "
            "doğru ve bağlama duyarlı bir yanıt ver.\n\n"
            f"{prompt}")

def persona_tr(prompt: str, country: str) -> str:
    return (f"{country} yaşayan ve o ülkenin geleneklerine, "
            f"göreneklerine ve günlük normlarına aşina biri gibi cevap ver. "
            f"Yanıtlarını, o kültürde insanların durumu genellikle nasıl anlayıp "
            f"ele alacağını yansıtacak şekilde oluştur.\n\n"
            f"{prompt}")

def uncertainty_tr(prompt: str) -> str:
    return (
        "Cevap vermeden önce, sorudan neyin çıkarılabileceğini ve neyin çıkarılamayacağını dikkatlice değerlendir. "
        "Kültürel ayrıntılar hakkında temelsiz varsayımlarda bulunmaktan kaçın. Kültürel bağlam belirsiz olduğunda "
        "veya kendine olan güvenin sınırlıysa, bu belirsizliği açıkça belirt ve temkinli bir şekilde yanıtla.\n\n"
        f"{prompt}")

def combined_tr(prompt: str, country: str) -> str:
    return ("Cevaplamadan önce adım adım düşün. Kültürel kavramları ve ilgili normları "
            "(örneğin sosyal, işyeri, aile) belirle ve kültürel bağlamı çıkar. "
            f"{country}’den bir yerel gibi cevap ver; gerçekçi gelenekleri, görenekleri ve beklentileri yansıt. "
            "Temelsiz varsayımlardan kaçın. Kültürel detaylar belirsizse bunu açıkça belirt ve temkinli yanıtla. "
            "Açık ve kültürel olarak uygun bir cevap ver.\n\n"
            f"{prompt}")


STRATEGIES = {
    "en": {"chain_of_thought": chain_of_thought_en, "persona": persona_en, "uncertainty": uncertainty_en, "combined": combined_en},
    "de": {"chain_of_thought": chain_of_thought_de, "persona": persona_de, "uncertainty": uncertainty_de, "combined": combined_de},
    "el": {"chain_of_thought": chain_of_thought_el, "persona": persona_el, "uncertainty": uncertainty_el, "combined": combined_el},
    "es": {"chain_of_thought": chain_of_thought_es, "persona": persona_es, "uncertainty": uncertainty_es, "combined": combined_es},
    "it": {"chain_of_thought": chain_of_thought_it, "persona": persona_it, "uncertainty": uncertainty_it, "combined": combined_it},
    "pl": {"chain_of_thought": chain_of_thought_pl, "persona": persona_pl, "uncertainty": uncertainty_pl, "combined": combined_pl},
    "ru": {"chain_of_thought": chain_of_thought_ru, "persona": persona_ru, "uncertainty": uncertainty_ru, "combined": combined_ru},
    "tr": {"chain_of_thought": chain_of_thought_tr, "persona": persona_tr, "uncertainty": uncertainty_tr, "combined": combined_tr},
}


def get_prompt_fn(strategy: str, language: str):
    if language not in STRATEGIES:
        raise ValueError(f"Unsupported language: {language!r}. Supported: {list(STRATEGIES)}")
    if strategy not in STRATEGIES[language]:
        raise ValueError(f"Unknown strategy: {strategy!r}. Supported: {list(STRATEGIES[language])}")
    return STRATEGIES[language][strategy]
