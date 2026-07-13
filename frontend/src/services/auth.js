import api from "./api";

// Login
export const login = async (credentials) => {

    const response = await api.post(
        "/auth/login",
        credentials
    );

    return response.data;
};

// Student Registration
export const registerStudent = async (formData) => {

    const response = await api.post(
        "/auth/register/student",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }
    );

    return response.data;
};

// Company Registration
export const registerCompany = async (data) => {

    const response = await api.post(
        "/auth/register/company",
        data
    );

    return response.data;
};

// Logged User Profile
export const getProfile = async () => {

    const response = await api.get(
        "/auth/profile"
    );

    return response.data;
};

// Update Student Profile
export const updateStudentProfile = async (data) => {

    const response = await api.put(
        "/auth/student/profile",
        data
    );

    return response.data;
};

// Upload Resume
export const uploadResume = async (file) => {

    const form = new FormData();

    form.append("resume", file);

    const response = await api.post(
        "/auth/student/resume",
        form,
        {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }
    );

    return response.data;
};

export const updateCompanyProfile = async(data)=>{

    const response = await api.put(

        "/auth/company/profile",

        data

    )

    return response.data

}