// Role-prompt: Create a JavaScript function to parse JSON, handle potential errors, and manipulate the data, ensuring the code is beginner-friendly with clear comments.

/**
 * Parses and manipulates a JSON string.
 * @param {string} jsonString - The JSON string to parse.
 * @returns {Object|Error} - The manipulated data object or an error object if parsing fails.
 */
function parseAndManipulateJSON(jsonString) {
    let data;

    // Attempt to parse the JSON string.
    try {
        data = JSON.parse(jsonString);  // Parsing the JSON string to an object.
    } catch (error) {
        console.error("Error parsing JSON:", error);  // Logging any parsing errors.
        return error;
    }

    // Check if data is an array of objects as expected and perform manipulation.
    if (Array.isArray(data)) {
        data.forEach((item, index) => {
            // Manipulate JSON data here as needed. This is just an example of adding a new property.
            item.newProperty = `newValue ${index + 1}`;
        });
    } else if (typeof data === 'object') {
        // If data is a single object, manipulate it here. This is an example of adding a new property.
        data.newProperty = 'newValue';
    } else {
        console.error("Unexpected JSON format: must be an array of objects or a single object.");  // Handling unexpected JSON structure.
        return new Error("Unexpected JSON format.");
    }

    return data;  // Return the manipulated data.
}

// Example usage of parseAndManipulateJSON function with a JSON string.
function main() {
    const jsonString = `
    [
        {"name": "John", "age": 30},
        {"name": "Doe", "age": 25}
    ]`;

    const result = parseAndManipulateJSON(jsonString);
    if (!(result instanceof Error)) {
        console.log("Manipulated JSON data:", result);
    }
}

main();  // Calling main function to execute the program.
