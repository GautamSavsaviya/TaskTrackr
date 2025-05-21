
## ✅ **Project: To-Do List App**

---

### 🔹 1. Project Title & Summary

**Name**: *TaskTrackr – Simple To-Do List*
**Summary**:
A personal task management app where users can create, update, and delete tasks. Tasks can be marked as complete or pending and filtered accordingly. This project focuses on basic CRUD operations using Django’s model, form, and view system.

---

### 🔹 2. Skill Level

**Beginner**

---

### 🔹 3. Learning Objectives

* Understand Django’s MTV architecture
* Practice CRUD with models and forms
* Use function-based views (FBVs)
* Work with template inheritance
* Use Django ModelForms for clean form handling

---

### 🔹 4. Functional Requirements

* ✅ User can add a new task (title, description, due date)
* ✅ Tasks are listed in reverse creation order
* ✅ User can mark a task as complete/incomplete
* ✅ User can update or delete a task
* ✅ Task list can be filtered (all, complete, pending)
* ✅ Basic form validation
* ✅ Optional: Add task categories or priorities

---

### 🔹 5. Non-Functional Requirements

* Fast load times for task lists
* Minimal UI with clean UX
* Code should follow Django best practices (DRY, clear naming)
* Responsive design (mobile/tablet friendly)

---

### 🔹 6. Technical Constraints

* No user authentication in this version (single-user usage)
* Must use Function-Based Views (FBVs)
* SQLite only
* No third-party UI or JS library (pure Django + HTML/CSS)

---

### 🔹 7. Topics Covered

* Django models
* Function-based views
* CRUD operations
* Forms & ModelForms
* Template inheritance
* Template filters (`date`, `length`, etc.)
* Static files
* Basic custom error handling

---

### 🔹 8. Tech Stack

* Python 3.10+
* Django 4.2+
* SQLite
* HTML + Bootstrap (optional for UI)
* Git for version control

---

### 🔹 9. Tools & Packages

* ✅ Internal:

  * `django`
  * `django-crispy-forms` (optional for better form rendering)
* ❌ External:

  * None required

---

### 🔹 10. DevOps & Deployment Steps (Optional)

🛠️ You can skip deployment, **or try this mini deploy if curious**:

**Optional Beginner Deployment Steps (Render):**

* Push code to GitHub
* Sign up at [https://render.com](https://render.com)
* Create a new Web Service
* Add `requirements.txt`, `Procfile`, `runtime.txt`
* Configure database = SQLite (or PostgreSQL if you want stretch goal)
* Set `ALLOWED_HOSTS` and `DEBUG=False` in `settings.py`
* Use `gunicorn` as the WSGI server

---

### 🔹 11. Project Duration Plan (2–3 hrs/day)

| Phase                    | Time    | Tasks                                                                               |
| ------------------------ | ------- | ----------------------------------------------------------------------------------- |
| 🧭 Planning & Setup      | Day 1   | - Create project + app<br>- Setup virtualenv & Git<br>- Setup base template, CSS    |
| 🧱 Models & Forms        | Day 2–3 | - Create `Task` model<br>- Create forms with `ModelForm`<br>- Setup migration       |
| 🔁 Views & Templates     | Day 4–6 | - List, Create, Update, Delete tasks<br>- Use CBVs if stretch goal<br>- Add filters |
| 🔬 Testing               | Day 7   | - Manual form & view testing<br>- Optional: add `unittest` test cases               |
| 🚀 Deployment (optional) | Day 8   | - Prepare `requirements.txt`<br>- Setup GitHub + Render                             |

Total Duration: **\~1 week** at 2–3 hours/day

---

### 🔹 12. Stretch Goals

* Add categories or priority levels
* Add simple authentication (login/logout/register)
* Add task due date sorting
* Add reminders via email (next project builds this out)

---

### 🔹 13. Evaluation Checklist ✅

| Area          | Criteria                                            |
| ------------- | --------------------------------------------------- |
| Functionality | All CRUD operations work                            |
| UI            | User can easily add/update tasks                    |
| Code          | Views follow DRY principles                         |
| Templates     | Inheritance works, no redundancy                    |
| Git           | Project is committed in logical steps               |
| Learning      | You can explain how ModelForm simplifies form logic |
