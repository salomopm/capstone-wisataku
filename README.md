

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


<table  align="center">
        <thead>
            <tr>
                <th>Welcome Page</th>
                <th>Register Page</th>
				        <th>Login Page</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187547756869472367/1.jpeg?ex=65974908&is=6584d408&hm=3b3eb2b99471cfbee5e9e70a38f6bedef912a7144a06adb36998c241287a17ea&=&format=webp&width=269&height=614" width="200"></a></p></td>
				<td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187548372140314685/2.jpeg?ex=6597499b&is=6584d49b&hm=e4cb572052b0c07a31dd2f3a347288319e517ba43cf75bde65ed6f3fc403786b&=&format=webp&width=269&height=614" width="200"></a></p></td>
				<td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187548652370149427/4.jpeg?ex=659749de&is=6584d4de&hm=e3c4e656bf8233c30b5c16e1ba069f312f1139cba6a48e5dfd43a61f5e8d33df&=&format=webp&width=269&height=614" width="200"></a></p></td>
            </tr>
        </tbody>
</table>

<table  align="center">
        <thead>
            <tr>
                <th>Main Page</th>
                <th>Detail Page</th>
				        <th>Map Page</th>
                <th>Profile Page</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187549361123631194/6.jpeg?ex=65974a87&is=6584d587&hm=e816749a36f7a5abc87d9afbf74287174917ec1ccff21ac8637ba6d88ec50d8f&=&format=webp&width=269&height=614" width="200"></a></p></td>
				        <td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187549563289079918/7.jpeg?ex=65974ab7&is=6584d5b7&hm=4c1817a103963207db5bd24950dc8085bd9bbd57d9da8994b7122c495d23a58f&=&format=webp&width=269&height=614" width="200"></a></p></td>
				        <td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187549827437973594/8.jpeg?ex=65974af6&is=6584d5f6&hm=c95171664877118f0145ba3de46dab0f27d6826b9efdf608ee2be3e21453ce99&=&format=webp&width=269&height=614" width="200"></a></p></td>
                <td><p align="center"><a href="" target="_blank"><img src="https://media.discordapp.net/attachments/1187547700158271569/1187550300492533860/10.jpeg?ex=65974b67&is=6584d667&hm=13aa4e37373d5f50bef88d90a4569327d137b3c7e1cddab3b5e809b1a3bcc66c&=&format=webp&width=269&height=613" width="200"></a></p></td>
            </tr>
        </tbody>
</table>




## Infrastructure Design


![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Mobile Development Documentation
- [WisataKu Design Figma](https://www.figma.com/file/N9FajbShIdmbClqFX5s9ZK/Wisataku?type=design&node-id=0%3A1&mode=design&t=G2BobOZjE1CqEvyM-1)
- [WisataKu SS and Demo Video](https://drive.google.com/drive/folders/1pQlYn_74a3YebzgOiCPfwPKrTmWjHI-S?usp=sharing)
- [WisataKu Apk](https://drive.google.com/drive/folders/1SvYpF_2Hsz8uUvT_uLkg7hFvCJ1l01EN?usp=sharing)


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

