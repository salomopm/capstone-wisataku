const bcrypt = require('bcrypt')
const users = require('./users');
const jwt = require('jsonwebtoken');
const JWT_SECRET = 'CH2-PS432';


const LoginUserHandler = async (request, h) => {
    const {email, password} = request.payload;

    var user = users.find(user => user.email === email)
    if (user === false) {
        return response.status(400).send('Cannot find user')
    }else if(user != null){
        try {
            if (await bcrypt.compare(password, user.hashedPassword)) {
              
              const userPayload = {
                email: user.email,
                nama: user.nama,
                role: user.role
              }
              

              const expiresIn = 60*60*1;

              const token = jwt.sign(userPayload, JWT_SECRET, {expiresIn: expiresIn})
              const decodedToken = jwt.verify(token, JWT_SECRET);
              console.log(decodedToken);
              const response = h.response({
                status: 'Success',
                message: 'Berhasil Authentikasi & Authorization',
                token: token
              });
              response.code(201);
              return response;
            } else {
              const response = h.response({
                status: 'Failed',
                message: 'Gagal Authentikasi & Authorization',
              });
              response.code(400);
              return response;
            }
          } catch (error) {
            console.error(error); // Log the error to the console
            response.status(500).send('Internal Server Error'); // Provide a more specific error message
          }
    }
    const response = h.response({
        status: 'Failed',
        message: 'Gagal menemukan user. Mohon isi data dengan benar',
        });
        response.code(400);
        return response;

};

const addUsersHandler = async (request, h) => {
    const {nama, email, password} = request.payload;
    
    const hashedPassword = await bcrypt.hash(password, 10)


    const newUsers = {nama, email, hashedPassword, role: "user"}
    var user = users.findIndex(user => user.nama === nama)
    if (user !== -1) {
      const response = h.response({
        status: 'fail',
        message: 'Nama telah diambil'
      });
      response.code(400);
      return response;
    }else if (newUsers.nama != null && newUsers.email != null && newUsers.hashedPassword != null) {
      const response = h.response({
        status: 'success',
        message: 'User berhasil ditambahkan',
      });
      response.code(201);
      users.push(newUsers);
      return response;
  }



    const response = h.response({
        status: 'fail',
        message: 'Gagal menambahkan User. Mohon isi data dengan benar',
        });
        response.code(400);
        return response;
};


const getAllUsersHandler = (request, h) => {

  const token = request.headers.authorization.split('Bearer ')[1];
  const decodedToken = jwt.decode(token, { complete: true });
  const { payload } = decodedToken;
  

  if (payload.role && payload.role == 'user') {
    const filteredUsers = users.map((user) => ({
      email: user.email,
      nama: user.nama,
      password: user.hashedPassword,
      role: user.role
    }));
    
    const response = h.response({
      status: 'success',
      data: {
        users: filteredUsers,
      },
    });
    response.code(200);
    return response;
  } else {
    const response = h.response({
      status: 'Failed',
      message: 'Access denied'
    });
    response.code(400);
    return response;
  }
};

module.exports = { addUsersHandler, LoginUserHandler, getAllUsersHandler };
