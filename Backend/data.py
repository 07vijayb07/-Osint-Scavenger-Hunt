challenges = [
    {
        "id": 1,
        "title": "Where is this café?",
        "difficulty": "Easy",
        "technique": "Visual clues",
        "points": 10,
        "question": "What suburb is this café located in?",
        "answer": [
            "Surfers Paradise",
            "surfers paradise"
        ],
        "image": "http://127.0.0.1:5007/images/image1.jpg",
        "metadata": "",
    },

    {
        "id": 2,
        "title": "Spot the country",
        "difficulty": "Easy",
        "technique": "Language recognition",
        "points": 10,
        "question": "Which country is this likely taken in?",
        "answer": [
            "France",
            "france"
        ],
        "image": "http://127.0.0.1:5007/images/image2.jpg",
        "metadata": "",
    },

    {
        "id": 3,
        "title": "Real or phishing?",
        "difficulty": "Medium",
        "technique": "Business verification",
        "points": 15,
        "question": "One click could compromise the company.Real or phishing?(Format: RealorPhishing_Exact Indicator)",
       "answer": [
    "Phishing_Mailid",
    "phishing_mailid",
    "Phishing_security@paypa1-verify.com",
    "phishing_security@paypa1-verify.com"
],
        "image": "http://127.0.0.1:5007/images/image3.jpg",
        "metadata": "",
    },

    {
        "id": 4,
        "title": " Transport OSINT challenge",
        "difficulty": "Easy-Moderate",
        "technique": "Transport OSINT",
        "points": 15,
        "question": "What is the earliest available tram to Helensvale station? (Format: HH:MM am)",
        "answer": [
            "04:52 am",
            "4:52 am",
            "04:52",
            "4:52"
        ],
        "image": "http://127.0.0.1:5007/images/image4.jpg",
        "metadata": "",
    },

    {
        "id": 5,
        "title": "Which image is taken during morning time of a day?",
        "difficulty": "Moderate",
        "technique": "Shadow analysis",
        "points": 15,
        "question": "Which image is taken during morning time of a day? (Format: IMAGE-A or IMAGE-B)",
        "answer": [
            "IMAGE-A",
            "Image-A",
            "image-a",
            "A"
        ],
        "image": "http://127.0.0.1:5007/images/image5.jpg",
        "metadata": "",
    },

    {
        "id": 6,
        "title": "Can you guess which bridge the photographer was on while taking this image?",
        "difficulty": "Moderate",
        "technique": "Geolocation clues",
        "points": 20,
        "question": "Can you guess which bridge the photographer was on while taking this image? (Format: NameOfBridge)",
        "answer": [
            "Kurilpa",
            "Kurilpa Bridge",
            "kurilpa",
            "kurilpa bridge"
        ],
        "image": "http://127.0.0.1:5007/images/image6.jpg",
        "metadata": "",
    },

    {
        "id": 7,
        "title": "Metadata analysis challenge",
        "difficulty": "Moderate",
        "technique": "Metadata analysis",
        "points": 20,
        "question": "Could you get the exact time and location this photo was taken? (Format: Location_HH:MM)",
        "answer": [
            "Kanyakumari_06:12",
            "kanyakumari_06:12",
            "Kanyakumari 06:12"
        ],
        "image": "http://127.0.0.1:5007/images/image7.jpg",
        "metadata": "",
    },

    {
        "id": 8,
        "title": "Cross-source verification",
        "difficulty": "Moderate-Hard",
        "technique": "Multi-source validation",
        "points": 20,
        "question": "When did the event take place? (Format: DD/MM/YYYY)",
        "answer": [
            "21/03/2026",
            "21-03-2026",
            "21/03/26"
        ],
        "image": "http://127.0.0.1:5007/images/image8.jpg",
        "metadata": "",
    },

    {
        "id": 9,
        "title": "Colour identification challenge",
        "difficulty": "Hard",
        "technique": "Multi-step OSINT",
        "points": 25,
        "question": "Can you get the general name of the colour in the given location? (Format: ColourName)",
        "answer": [
            "Blue grey",
            "Blue Grey",
            "Cool Grey",
            "Slate Grey",
            "Grey",
            "Gray"
        ],
        "image": "http://127.0.0.1:5007/images/image9.jpg",
        "metadata": "",
    },

    {
        "id": 10,
        "title": "Full investigation challenge",
        "difficulty": "Hard",
        "technique": "Combined OSINT",
        "points": 30,
        "question": "From the provided image can you find the carrier's (i) IMO(Numbers only) (ii)Name of carrier (iii) Flag (Country) (iv) In the respective country, what was happening during the years 1946 to 1958 (Answer Format: IMO_Name of carrier_Historical Event)",
        "answer": [
        "1040069_Dubai sky_Marshall Islands_Nuclear Testing" ,
        "1040069_Dubai sky_Marshall Islands_Atomic Bomb Test"
        ],
        "image": "http://127.0.0.1:5007/images/image10.jpg",
        "metadata": "",
    }
]