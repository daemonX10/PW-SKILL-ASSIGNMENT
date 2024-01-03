import React from "react"
import { useNavigate } from "react-router-dom"

export const ImageCard=({imageUrl,id})=>{
    const navigate=useNavigate()
    
    const redirectToPage = () => {
        navigate(`/${id}`)
    }

    return(
    <div>
            <img src={imageUrl} onClick={redirectToPage} alt="" />
    </div>
    )
}

// TODO: 3. Create a component called ImageCard.jsx which will be used to display the image in the home page.