def main() -> None:
    print("Hello from remote-job-research-agent!")


skills = ["Python", "FastAPI", "Docker"]

skills.append("PostgreSQL")

print(skills[0])
print(skills[-1])
print(skills[:2])

lower_skills = [skill.lower() for skill in skills]
print(lower_skills)

python_skills = [skill.lower() for skill in skills if "python" in skill.lower()]
print(python_skills)


skill_counts = {
    "python": 3,
    "docker": 2,
    "fastapi": 1,
}

print(skill_counts["python"])
print(skill_counts.get("aws", 0))


words = ["python", "docker", "python", "fastapi"]

unique_words = set(words)

print(unique_words)
print(len(unique_words))
print("python" in unique_words)


skill_item = ("python", 3)

skill, count = skill_item

print(skill)
print(count)


for skill, count in skill_counts.items():
    print(f"{skill}: {count}")


file_name = "sample_jd.txt"
word_count = 100

print(f"File: {file_name}")
print(f"Words: {word_count}")
