FROM python
WORKDIR /test_project
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s /test_project/tests/406_test_user_auth.py

# docker run --rm --mount type=bind, src= C:\Users\mikhail.osinovskiy\PycharmProjects\LearnQA_Python_API,targeet=/tests_project pytest_runner
