import api from "./api"

export const createDrive = async(data)=>{

    const response = await api.post(

        "/company/drives",

        data

    )

    return response.data

}


export const getDrives = async()=>{

    const response = await api.get(

        "/company/drives"

    )

    return response.data

}



export const closeDrive = async(id)=>{

    const response = await api.put(

        `/company/drives/${id}/close`

    )

    return response.data

}

export const getApplications = async(driveId)=>{

    const response = await api.get(

        `/company/drives/${driveId}/applications`

    )

    return response.data

}





export const updateApplicationStatus = async(

    id,

    status

)=>{


    const response = await api.put(

        `/company/applications/${id}/status`,

        {

            status

        }

    )


    return response.data

}

export const getStudentDetails = async(id)=>{

    const response = await api.get(

        `/company/students/${id}`

    )

    return response.data

}

export const getCompanyProfile = async()=>{

    const response = await api.get(

        "/company/profile"

    )

    return response.data

}

export const getSelectedStudents = async()=>{

    const response = await api.get(

        "/company/selected-students"

    )

    return response.data

}

export const getDashboard = async()=>{

    const response = await api.get(

        "/company/dashboard"

    )

    return response.data

}