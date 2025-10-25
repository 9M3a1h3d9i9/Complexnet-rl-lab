# Complexnet-rl-lab
Reinforcement Learning Laboratory for Complex Networks













Complexnet-rl-lab/
│── src/                # کدهای اصلی (algorithms, utils)
│── notebooks/          # نوت‌بوک‌های مرحله‌ای و آزمایشی
│── tests/              # تست‌های واحد (unit tests)
│── data/               # داده‌ها (مثلاً Anaheim)
│── results/            # خروجی‌ها (log, txt, plots)
│── requirements.txt    # لیست پکیج‌ها
│── README.md           # توضیحات پروژه
│── .gitignore



Branching Strategy:

main → نسخه پایدار

feature/nx-graph → ساخت گراف ۱۵ نودی

feature/edmonds-karp → پیاده‌سازی الگوریتم max-flow

feature/gomory-hu → پیاده‌سازی درخت گوموری–هو

docs/notebook → نوت‌بوک مرحله‌ای و گزارش

tests/unit → تست‌های واحد

مثال:
git checkout -b feature/nx-graph

(برای همه شاخه انجام شده ✔)



Stepwise Development:
for example :::

git add src/nx_graph_15.py
git commit -m "feat(nx-graph): add 15-node directed graph with capacities"
git push origin feature/nx-graph

 . . . 



 Testing and CI/CD :

 pytest tests/

 git add tests/
 git commit pm "test: add unit tests for Ek and Gh implementations"



Phase 5 ) Merge & Tag :

وقتی هر شاخه کامل شد:

bash
git checkout main
git merge --no-ff feature/nx-graph -m "merge: add 15-node graph builder"
git merge --no-ff feature/edmonds-karp -m "merge: add manual EK implementation"
git merge --no-ff feature/gomory-hu -m "merge: add manual GH tree"
git merge --no-ff docs/notebook -m "merge: add step-by-step notebook"
git push
git tag v0.1-gh-manual
git push origin v0.1-gh-manual



