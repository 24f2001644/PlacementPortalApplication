import api from "./api"



/*
====================================
 STUDENT DASHBOARD
====================================
*/


export const getStudentDashboard = async()=>{


    const response = await api.get(

        "/student/dashboard"

    )


    return response.data


}

export const getProfile = async()=>{

    const response = await api.get(

        "/student/profile"

    )

    return response.data

}

export const updateProfile = async(data)=>{

    const response = await api.put(

        "/student/profile",

        data

    )

    return response.data

}

export const getDrives = async(search="")=>{

    const response = await api.get(

        "/student/drives",

        {

            params:{

                search

            }

        }

    )

    return response.data

}

export const getDriveDetails = async(id)=>{

    const response = await api.get(

        `/student/drives/${id}`

    )

    return response.data

}



export const applyForDrive = async(id)=>{

    const response = await api.post(

        `/student/drives/${id}/apply`

    )

    return response.data

}

export const getApplications = async()=>{

    const response = await api.get(

        "/student/applications"

    )

    return response.data

}



export const withdrawApplication = async(id)=>{

    const response = await api.delete(

        `/student/applications/${id}/withdraw`

    )

    return response.data

}

export const exportApplications = async()=>{

    return await api.get(

        "/student/export",

        {

            responseType:"blob"

        }

    )

}
