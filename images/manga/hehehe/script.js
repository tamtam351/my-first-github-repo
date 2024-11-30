async function getrandomimage(){
    try{
      const reponse =  await fetch("https://api.waifu.pics/sfw/waifu")
    if(!response.ok){
        throw new Error('Network response was not ok')
    }

    const data = await response.json()
    const imageurl = data.url;
    
    const imgElement = document.getElementById('animeImage')
    imgElement.src(imageurl)
    
    } catch (error){
        console.error('Error fetching anime image:', error)
    }
  }
