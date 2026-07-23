<script setup>

import { ref } from "vue"

import AdminSidebar from "../../components/admin/AdminSidebar.vue"
import AdminNavbar from "../../components/admin/AdminNavbar.vue"
import AdminPageHeader from "../../components/admin/AdminPageHeader.vue"
import AdminSectionCard from "../../components/admin/AdminSectionCard.vue"

import {
    getNotifications,
    createNotification
} from "../../services/notificationService"



const title = ref("")

const message = ref("")

const notificationType = ref("GENERAL")

const target = ref("ALL")

const sending = ref(false)



async function send() {

    if (
        !title.value.trim() ||
        !message.value.trim()
    ) {

        alert("Please fill all fields")

        return

    }

    sending.value = true

    try {

        const response = await createNotification({

            title: title.value,

            message: message.value,

            notification_type: notificationType.value,

            target: target.value

        })

        console.log(response)

        alert(response.data?.message || "Notification sent successfully")

        title.value = ""

        message.value = ""

        notificationType.value = "GENERAL"

        target.value = "ALL"

    }

    catch (error) {

        console.error(error)

        alert("Unable to send notification")

    }

    finally {

        sending.value = false

    }

}

</script>

<template>

<div class="admin-layout">

    <AdminSidebar />

    <div class="admin-content">

        <AdminNavbar />

        <div class="container-fluid mt-4">

            <AdminPageHeader

                title="Notifications"

                subtitle="Send notifications to students and companies"

            />

            <div class="row justify-content-center">

                <div class="col-lg-8">

                    <AdminSectionCard
                        title="Create Notification"
                    >

                        <div class="mb-3">

                            <label class="form-label">

                                Title

                            </label>

                            <input

                                v-model="title"

                                class="form-control"

                                placeholder="Enter notification title"

                            />

                        </div>



                        <div class="mb-3">

                            <label class="form-label">

                                Message

                            </label>

                            <textarea

                                v-model="message"

                                rows="6"

                                class="form-control"

                                placeholder="Write notification"

                            ></textarea>

                        </div>



                        <div class="mb-3">

                            <label class="form-label">

                                Notification Type

                            </label>

                            <select

                                v-model="notificationType"

                                class="form-select"

                            >

                                <option value="GENERAL">

                                    General

                                </option>

                                <option value="PLACEMENT">

                                    Placement

                                </option>

                                <option value="REMINDER">

                                    Reminder

                                </option>

                                <option value="EXPORT">

                                    Export

                                </option>

                            </select>

                        </div>



                        <div class="mb-4">

                            <label class="form-label">

                                Send To

                            </label>

                            <select

                                v-model="target"

                                class="form-select"

                            >

                                <option value="ALL">

                                    All Users

                                </option>

                                <option value="STUDENT">

                                    Students

                                </option>

                                <option value="COMPANY">

                                    Companies

                                </option>

                            </select>

                        </div>



                        <button

                            class="btn btn-primary w-100"

                            @click="send"

                            :disabled="sending"

                        >

                            <i class="bi bi-send me-2"></i>

                            {{ sending ? "Sending..." : "Send Notification" }}

                        </button>

                    </AdminSectionCard>

                </div>

            </div>

        </div>

    </div>

</div>

</template>

<style scoped>

.admin-layout{

    display:flex;

    min-height:100vh;

    background:#f8fafc;

}

.admin-content{

    flex:1;

    display:flex;

    flex-direction:column;

}

.container-fluid{

    padding:28px;

}

.form-label{

    font-weight:600;

    color:#334155;

}

.form-control,

.form-select{

    border-radius:10px;

}

textarea{

    resize:none;

}

.btn{

    height:48px;

    font-weight:600;

}

@media(max-width:992px){

    .admin-layout{

        flex-direction:column;

    }

}

@media(max-width:768px){

    .container-fluid{

        padding:18px;

    }

}

</style>