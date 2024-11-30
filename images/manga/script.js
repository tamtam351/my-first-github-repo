// Function to fetch and display random anime image
// async function getRandomAnimeImage() {
//     try {
//       // Fetch a random anime image from the Waifu.pics API
//       const response = await fetch('https://api.waifu.pics/sfw/waifu');
      
//       // Check if the request was successful
//       if (!response.ok) {
//         throw new Error('Network response was not ok');
//       }
      
//       // Parse the JSON response
//       const data = await response.json();
      
//       // Extract the image URL from the API response
//       const imageUrl = data.url;
      
//       // Get the image element in the HTML (make sure it exists)
//       const imgElement = document.getElementById('animeImage');
      
//       // Set the src attribute of the image element to the new image URL
//       imgElement.src = imageUrl;
      
//       // Optional: Log the image URL for debugging
//       console.log('Random Anime Image:', imageUrl);
//     } catch (error) {
//       window.alert('Error fetching anime image:', error);
//     }
//   }
  
//   // Call the function to load the image
//   getRandomAnimeImage();
  


async function getRandomAnimeImage() {
    try{
        const response = await fetch("'https://api.waifu.pics/sfw/waifu'")
    if(!response.ok){
        throw new Error('Network response was not ok')
    }
    const data = await response.json()
    const imageurl = data.url;

    const imgElement= document.getElementById('animeImage')
    imgElement.src=imageurl;

    } catch (error){
        window.alert("there's a problem fetching anime image",error)
    }
}

getRandomAnimeImage();