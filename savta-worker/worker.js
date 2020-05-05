var http = require('http');
var AccessToken = require('twilio').jwt.AccessToken;
var VideoGrant = AccessToken.VideoGrant;

const accountSid = 'ACc65ca087acb6fadbe2afd37380ab3559';
const apiKey = 'SK81936cf9f87dd96504dab55c4d977f8a';
const authToken = 'Yvs3hCmH5kU6hN2tEwwvPYtRg5FDk0ts';

addEventListener('fetch', event => {
event.respondWith(handleRequest(event.request))
})

/**
 * Respond to the request
 * @param {Request} request
 */
async function handleRequest(request) {
    const params = {}
    const url = new URL(request.url);
    const queryString = url.search.slice(1).split('&')

    queryString.forEach(item => {
        const kv = item.split('=')
        if (kv[0]) params[kv[0]] = kv[1] || true
    })
    if (url.pathname === "/token" && request.method === "GET") {
    
    var identity = params['identity'];
    if (!identity) {
        throw "Couldn't find identity in url parameter!";
    }

    // Create an access token which we will sign and return to the client,
    // containing the grant we just created.
    
    var token = new AccessToken(
    accountSid,
    apiKey,
    authToken,
    { ttl: 14400 }
    );

    // Assign the generated identity to the token.
    token.identity = identity;

    // Grant the access token Twilio Video capabilities.
    var grant = new VideoGrant();
    grant.room = "savta";
    token.addGrant(grant);

    // Serialize the token to a JWT string and include it in a JSON response.
    return new Response(token.toJwt(), {status: 200});
}
return new Response('Not Found', {status: 404});
}