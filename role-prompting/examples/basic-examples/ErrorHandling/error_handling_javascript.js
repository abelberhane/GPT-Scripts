// Role-prompt: Create a JavaScript function that makes an HTTP request to a REST API and handles potential errors gracefully. The function should demonstrate catching various types of errors, logging descriptive error messages, and ensuring the program continues running smoothly even when an error is encountered.

const axios = require('axios');

/**
 * This function makes an HTTP request to a specified URL and handles any errors that may occur during the request.
 * @param {string} url - The URL of the REST API to request data from.
 */
async function fetchData(url) {
    try {
        // Attempt to send a GET request to the specified URL.
        const response = await axios.get(url);

        // Process the response if the request was successful.
        console.log(response.data);
    } catch (error) {
        // The role-prompt specifically requires handling various types of errors, guiding GitHub Copilot to generate this comprehensive error-handling block.

        if (error.response) {
            // The request was made and the server responded with a status code that falls out of the range of 2xx.
            // Logging detailed information about the response helps in debugging, which is a benefit outlined in the role-prompt.
            console.error('The server responded with an unexpected status:', error.response.status);
            console.error('Response body:', error.response.data);
        } else if (error.request) {
            // The request was made but no response was received, an instance of a network error.
            // Role-prompting ensures these distinct scenarios are handled separately, improving error feedback.
            console.error('No response received from the server:', error.request);
        } else {
            // An error occurred while setting up the request.
            // This catch-all block ensures that even unexpected errors are caught and logged, ensuring the program's robustness as specified in the role-prompt.
            console.error('Error setting up the request:', error.message);
        }
    } finally {
        // The finally block is executed after try and catch, regardless of the outcome.
        // Including this ensures that the program continues running smoothly, a key aspect mentioned in the role-prompt.
        console.log('Finished requesting data from:', url);
    }
}

// Execute the function with a test URL.
fetchData('https://api.example.com/data')
  .then(() => console.log('Data retrieval attempt completed.')); // This line ensures the program continues even if there's an error, fulfilling the role-prompt's requirement for smooth continuation.

