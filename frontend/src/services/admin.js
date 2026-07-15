import api from "./api";


export const getStudentDetails = async(id)=>{

    const response = await api.get(

        `/admin/students/${id}`

    );

    return response.data;

};

/* ==========================================================
   DASHBOARD
========================================================== */

export const getDashboard = async () => {

    const response = await api.get(
        "/admin/dashboard"
    );

    return response.data;
};


/* ==========================================================
   COMPANY MANAGEMENT
========================================================== */

export const getCompanies = async (search = "") => {

    const response = await api.get(
        "/admin/companies",
        {
            params: { search }
        }
    );

    return response.data;
};


export const approveCompany = async (userId) => {

    const response = await api.put(
        `/admin/companies/${userId}/approve`
    );

    return response.data;
};


export const rejectCompany = async (userId) => {

    const response = await api.delete(
        `/admin/companies/${userId}/reject`
    );

    return response.data;
};


export const blacklistCompany = async (userId) => {

    const response = await api.put(
        `/admin/companies/${userId}/blacklist`
    );

    return response.data;
};


/* ==========================================================
   STUDENT MANAGEMENT
========================================================== */

export const getStudents = async (search = "") => {

    const response = await api.get(
        "/admin/students",
        {
            params: { search }
        }
    );

    return response.data;
};


export const toggleStudentStatus = async (userId) => {

    const response = await api.put(
        `/admin/students/${userId}/toggle`
    );

    return response.data;
};


/* ==========================================================
   PLACEMENT DRIVE MANAGEMENT
========================================================== */

export const getDrives = async (search = "") => {

    const response = await api.get(
        "/admin/drives",
        {
            params: { search }
        }
    );

    return response.data;
};


export const approveDrive = async (driveId) => {

    const response = await api.put(
        `/admin/drives/${driveId}/approve`
    );

    return response.data;
};


export const rejectDrive = async (driveId) => {

    const response = await api.put(
        `/admin/drives/${driveId}/reject`
    );

    return response.data;
};


export const closeDrive = async (driveId) => {

    const response = await api.put(
        `/admin/drives/${driveId}/close`
    );

    return response.data;
};


/* ==========================================================
   APPLICATION MANAGEMENT
========================================================== */

export const getApplications = async (

    search = "",

    status = ""

) => {

    const response = await api.get(

        "/admin/applications",

        {

            params: {

                search,

                status

            }

        }

    )

    return response.data

}


export const updateApplicationStatus = async (

    applicationId,

    status

) => {

    const response = await api.put(

        `/admin/applications/${applicationId}/status`,

        {
            status
        }

    );

    return response.data;
};


/* ==========================================================
   ANALYTICS
========================================================== */

export const getStatistics = async () => {

    const response = await api.get(
        "/admin/statistics"
    );

    return response.data;
};


export const getDriveDetails = async (driveId) => {

    const response = await api.get(

        `/admin/drives/${driveId}`

    )

    return response.data

}


/* ==========================================================
   NOTIFICATIONS
========================================================== */


export const getNotifications = async () => {

    const response = await api.get(
        "/admin/notifications"
    );

    return response.data;

};



export const createNotification = async (data) => {

    const response = await api.post(
        "/admin/notifications",
        data
    );

    return response.data;

};


export async function exportCSV() {

    const response = await api.post(

        "/admin/exports",

        {
            student_id: 1
        }

    )

    return response.data

}


export async function getExportStatus(jobId){

    const response = await api.get(

        `/admin/exports/${jobId}`

    )

    return response.data

}

export async function downloadCSV(jobId){

    const response = await api.get(
        `/admin/exports/${jobId}/download`,
        {
            responseType: "blob"
        }
    )

    return response.data

}