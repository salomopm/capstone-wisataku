const Hapi = require('@hapi/hapi');
const routes = require('./routes');
const HapiAuthJWT2 = require('hapi-auth-jwt2');
const JWT_SECRET = 'CH2-PS432';


const init = async () => {

  const server = Hapi.server({
    port: 3000,
    host: 'localhost',
    routes: {
      cors: {
        origin: ['*'],
      },
    },
  });
  await server.register(HapiAuthJWT2);

  server.auth.strategy('jwt', 'jwt', {
    key: JWT_SECRET,
    algorithm: 'HS256',
    validate: async (decoded, request) => {
        return { isValid: true, credentials: decoded };
    }
  });

  server.auth.default('jwt');

  server.route(routes);
  
  await server.start();
  console.log(`Server berjalan pada ${server.info.uri}`);
};
   
  init();





