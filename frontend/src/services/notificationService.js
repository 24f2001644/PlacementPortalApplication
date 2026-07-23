import axios from "axios";

const API = "http://127.0.0.1:5000/api/notifications";

function getToken() {
    return localStorage.getItem("token");
}

export async function getNotifications() {
    const response = await axios.get(API, {
        headers: {
            Authorization: `Bearer ${getToken()}`
        }
    });

    return response.data;
}

export async function getUnreadCount() {
    const response = await axios.get(`${API}/unread-count`, {
        headers: {
            Authorization: `Bearer ${getToken()}`
        }
    });

    return response.data;
}

export function markAsRead(notificationId) {
    return axios.put(
        `${API}/${notificationId}/read`,
        {},
        {
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );
}

export function deleteNotification(notificationId) {
    return axios.delete(
        `${API}/${notificationId}`,
        {
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );
}


export function createNotification(data) {
    return axios.post(
        API,
        data,
        {
            headers: {
                Authorization: `Bearer ${getToken()}`
            }
        }
    );
}