<script setup>

import { ref, onMounted } from "vue"

import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"
import CompanySectionCard from "../../components/company/CompanySectionCard.vue"
import CompanyEmptyState from "../../components/company/CompanyEmptyState.vue"

import {
    getNotifications,
    markAsRead,
    deleteNotification
} from "../../services/notificationService"

const notifications = ref([])
const loading = ref(true)

async function loadNotifications() {

    loading.value = true

    try {

        const response = await getNotifications()

        console.log("FULL RESPONSE", response)

        notifications.value = response

        console.log("notifications", notifications.value)

        console.log("length", notifications.value.length)

    }

    catch (err) {

        console.error(err)

    }

    finally {

        loading.value = false

    }

}

async function readNotification(notificationId) {

    try {

        await markAsRead(notificationId)

        loadNotifications()

    }

    catch (error) {

        console.error(error)

    }

}

async function removeNotification(notificationId) {

    if (!confirm("Delete this notification?")) {

        return

    }

    try {

        await deleteNotification(notificationId)

        loadNotifications()

    }

    catch (error) {

        console.error(error)

    }

}

onMounted(() => {

    loadNotifications()

})

</script>

<template>

<div class="company-layout">

    <CompanySidebar />

    <div class="company-content">

        <CompanyNavbar />

        <div class="container-fluid mt-4">

            <CompanyPageHeader
                title="Notifications"
                subtitle="Latest notifications from Admin"
            />

            <CompanySectionCard
                title="My Notifications"
            >

                <div
                    v-if="loading"
                    class="text-center py-5"
                >
                    Loading...
                </div>

                <template v-else>

                    <CompanyEmptyState
                        v-if="notifications.length === 0"
                        message="No notifications available"
                    />

                    <div
                        v-for="notification in notifications"
                        :key="notification.notification_id"
                        class="notification-card"
                        :class="{
                            unread: !notification.is_read
                        }"
                    >

                        <div
                            class="d-flex justify-content-between align-items-start"
                        >

                            <div>

                                <h5>

                                    {{ notification.title }}

                                </h5>

                                <span class="badge bg-primary">

                                    {{ notification.notification_type }}

                                </span>

                            </div>

                            <small>

                                {{ new Date(notification.created_at).toLocaleString() }}

                            </small>

                        </div>

                        <p class="mt-3 mb-3">

                            {{ notification.message }}

                        </p>

                        <div class="d-flex gap-2">

                            <button

                                v-if="!notification.is_read"

                                class="btn btn-success btn-sm"

                                @click="readNotification(notification.notification_id)"

                            >

                                Mark Read

                            </button>

                            <button

                                class="btn btn-danger btn-sm"

                                @click="removeNotification(notification.notification_id)"

                            >

                                Delete

                            </button>

                        </div>

                    </div>

                </template>

            </CompanySectionCard>

        </div>

    </div>

</div>

</template>

<style scoped>

.company-layout{

    display:flex;

    min-height:100vh;

    background:#f8fafc;

}

.company-content{

    flex:1;

}

.container-fluid{

    padding:25px;

}

.notification-card{

    border:1px solid #e2e8f0;

    border-radius:12px;

    padding:18px;

    margin-bottom:18px;

    background:white;

    transition:.2s;

}

.notification-card.unread{

    border-left:6px solid #2563eb;

    background:#eff6ff;

}

.notification-card h5{

    margin-bottom:6px;

    font-weight:600;

}

.notification-card p{

    color:#475569;

}

</style>