

# WisataKu


WisataKu is a machine learning based mobile application that is intended to be able to provide suggestion to users regarding travel destinations in certain location. WisataKu can be used by any people who wants some advice regarding travel destinations.






## CH2-PS432 Members




| Nama                          | Path                | Bangkit ID  |
| :--------                     | :-------            | :-----------|
| Seraf Adonai Rafanelli Patai  | Machine Learning    | M299BSY1818 |
| Muhammad Fahri Almasah        | Machine Learning    | M200BSY1023 |
| Ferdi Hasan                   | Machine Learning    | M200BSY0333 |
| Salomo Polanco                | Cloud Computing     | C312BSY4010 |
| Andreas Domenico Situmorang   | Cloud Computing     | C312BSY4020 |
| Muhammad Rizky Pratama        | Mobile Development  | A547BKY4485 |
| Tri Yulianto                  | Mobile Development  | A312BSY2929 |






## Screenshots


![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)




## Infrastructure Design


![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Machine Learning Model Installation
Steps to install Machine Learning Model locally


## Machine Learning Install Requirements
- [Documentation](https://linktodocumentation)
- [Documentation](https://linktodocumentation)
- [Documentation](https://linktodocumentation)


## Documentation


[Documentation](https://linktodocumentation)


## Cloud Computing Back-End Installation
Steps to install Cloud Computing Back-End Server




### Install Requirements


- [Install Node JS and NPM](https://kinsta.com/blog/how-to-install-node-js/)
- [Install PM2](https://pm2.keymetrics.io/docs/usage/quick-start/)




### Node JS package.json Installations Requirements


Packages that are needed to be installed:


- @Hapi/Hapi
- bcrypt
- hapi-auth-jwt2
- jsonwebtoken
- mysql


First you have to clone this repositroy
```bash
  git clone https://github.com/salomopm/capstone-wisataku.git
```
Go to the repository
```bash
  cd capstone-wisataku/cc/APIauth
```
And then install packages with npm:


```bash
  npm install [package]
```
Start the API server


- Run in Development
```bash
  npm run dev-start
```


- Run in Production
```bash
  npm run prod-start
```




## How to deploy the code to Google Cloud


### Requirements


- **VPC**


  All instances that will be created have to be in the same network and zone


- **Cloud SQL for MySQL**


  The database and the query is in MySQL format so you need to create Cloud SQL MySQL based.


- **Compute Engine**


  Build an engine that is capable to run the API.


### Cloud Configurations


- **Cloud SQL**


  You have to set the instance to be able to be access publicly by make it 0.0.0.0/0


- **Compute Engine**


  Change the Server IP to the public IP of the Compute Engine so the Mobile Application can access the API. Set the IP to access the database to the public IP of the Cloud SQL Instance and set the credentials too.


- **Firewall Rules**


  Create a firewall rule that allow ingress from 0.0.0.0/0




## wisataKu Authentication and Authorization API Reference


#### Register


```http
  POST /register
```


| Parameter           | Type     | Description                |
| :--------           | :------- | :------------------------- |
| `application/json`  | `string` | This endpoint is used for registration. The payload contains name, email and password. This endpoint will query the databse to check is the email is taken|


#### Login (authentication and authorization)


```http
  POST /login
```


| Parameter               | Type     | Description                       |
| :--------               | :------- | :-------------------------------- |
| `application/json`      | `string` | This end point is for authentication and also authorization. The endpoint will query the database and will do bcrypt comparations between payload's password and the database's password. If the credentials is right then the use will be given a JWT token. |


#### Get Users


```http
  GET /users
```


| Parameter               | Type     | Description                       |
| :--------               | :------- | :-------------------------------- |
| `application/json`      | `string` | This endpoint is for listing all the user that has registered. This endpoint can only be accessed by user with admin role |

## wisataKu Recommendation API Reference

```http
  GET /
```


| Parameter               | Type     | Description                       |
| :--------               | :------- | :-------------------------------- |
| `application/json`      | `string` | This endpoint will give response in json format about Recommendation places in all places that is under this mobile application's database scope|

```http
  POST /recommend_Place
```

| Parameter               | Type     | Description                       |
| :--------               | :------- | :-------------------------------- |
| `application/json`      | `string` | This endpoint will response about similiar places that is being searched by the user. So the user will input a name place (for the places's name has to be in the same format like in the database) and there will be output of places that is similar|

