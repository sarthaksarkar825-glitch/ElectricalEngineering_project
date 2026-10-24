import os
import pandas as pd

# 1. Complete 30-Chapter Page Range Map (PDF Page Numbers)
ALL_CHAPTERS_MAP = {
    "Chapter 1: Elementary Concepts and Definitions": (19, 51),
    "Chapter 2: Fundamental Laws of Electric Circuits, Resistive Circuits": (52, 95),
    "Chapter 3: Steady-State Analysis for Sinusoidal Excitation": (96, 161),
    "Chapter 4: Three-Phase Circuits": (162, 184),
    "Chapter 5: Magnetic Circuits": (185, 215),
    "Chapter 6: Transformers": (216, 257),
    "Chapter 7: dc Machines": (258, 305),
    "Chapter 8: Synchronous Machine-Generator and Motor": (306, 351),
    "Chapter 9: Induction Motor": (352, 386),
    "Chapter 10: Fractional kW Motors": (387, 396),
    "Chapter 11: Measuring Instruments": (397, 428),
    "Chapter 12: Power Systems": (429, 456),
    "Chapter 13: Semiconductors": (457, 466),
    "Chapter 14: Diodes and Applications": (467, 497),
    "Chapter 15: Bipolar Junction Transistor (BJT) and Other Devices": (498, 527),
    "Chapter 16: Field Effect Transistors (FETs)": (528, 553),
    "Chapter 17: Small-Signal Model of Transistors and Amplifiers": (554, 590),
    "Chapter 18: Op-Amp": (591, 614),
    "Chapter 19: Feedback Amplifiers and Oscillators": (615, 624),
    "Chapter 20: Regulated Power Supplies": (625, 634),
    "Chapter 21: Digital Logic": (635, 656),
    "Chapter 22: Digital Electronics": (657, 690),
    "Chapter 23: Boolean Algebra and Combinational Circuits": (691, 712),
    "Chapter 24: Flip-Flops": (713, 727),
    "Chapter 25: Registers and Counters": (728, 741),
    "Chapter 26: Digital to Analog and Analog to Digital Converters": (742, 755),
    "Chapter 27: Transducers": (756, 768),
    "Chapter 28: Basics of Computers": (769, 790),
    "Chapter 29: Clock and Timing Circuits": (791, 798),
    "Chapter 30: Communication Engineering": (799, 830),
}

# 2. Build the Hierarchical Nested Dictionary
# Schema: { Chapter: { Page/Subtopic: "all_book_pages/page_XXXX.jpg" } }
full_book_db = {}
for chap_name, (start_page, end_page) in ALL_CHAPTERS_MAP.items():
    full_book_db[chap_name] = {
        f"Page {p}": f"all_book_pages/page_{p:04d}.jpg"
        for p in range(start_page, end_page + 1)
    }

# 3. Flatten the Nested Dictionary into Tabular Records
records = []
for chapter, subtopics in full_book_db.items():
    for subtopic, img_data in subtopics.items():
        if isinstance(img_data, list):
            for idx, img_path in enumerate(img_data, start=1):
                records.append({
                    "Chapter": chapter,
                    "Subtopic": subtopic,
                    "Page Index": idx,
                    "Image Path": img_path,
                    "File Exists": os.path.exists(img_path),
                })
        else:
            records.append({
                "Chapter": chapter,
                "Subtopic": subtopic,
                "Page Index": 1,
                "Image Path": img_data,
                "File Exists": os.path.exists(img_data),
            })

# 4. Export to CSV
output_csv = "all_chapters_index.csv"
df = pd.DataFrame(records)
df.to_csv(output_csv, index=False)

print(f"\n[Done] Successfully converted nested dictionary to CSV!")
print(f"File created: '{output_csv}' with {len(df)} rows.")