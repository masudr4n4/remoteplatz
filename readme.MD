### RemotePlatz
Install dependencies
```
pip install -r requirements.txt
```
Run the command to execute all the test cases
```
pytest --html=reports/report.html --self-contained-html
```


covered Area:<br>
* auth/token/ (client/dev)
* auth/signup/ (client/dev)
* auth/countries/
* auth/cities/?country={country_id}
* jobs/get_talent_jobs/
* jobs/ (create job)
* jobs/applications/ (apply job)
* jobs/{job_id} (job details)
* jobs/get_client_jobs/
* invitations/
* talents/{talent_id}
* talents/?technologies={tech_id}