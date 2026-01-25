function generateText(prompt) {
  // Create a Vertex Generative AI request.
  const request = {
    key: 'YOUR_API_KEY',
    prompt: prompt,
  };

  // Make the request to the Vertex Generative AI API.
  const response = await fetch('https://aiplatform.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/YOUR_LOCATION/models/YOUR_MODEL_ID/generate', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${request.key}`,
    },
    body: JSON.stringify(request),
  });

  // Get the generated text from the response.
  const generatedText = await response.json();

  // Return the generated text.
  return generatedText.text;
}
