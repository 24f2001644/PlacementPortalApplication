<script setup>

import { ref, onMounted } from "vue"

import CompanySidebar from "../../components/company/CompanySidebar.vue"
import CompanyNavbar from "../../components/company/CompanyNavbar.vue"
import CompanyPageHeader from "../../components/company/CompanyPageHeader.vue"
import CompanySectionCard from "../../components/company/CompanySectionCard.vue"
import CompanyLoading from "../../components/company/CompanyLoading.vue"

import { getProfile } from "../../services/auth"

const loading = ref(true)

const company = ref({

    company_name:"",

    industry:"",

    website:"",

    location:"",

    hr_name:"",

    hr_email:"",

    hr_phone:"",

    description:""

})

async function loadProfile(){

    loading.value = true

    try{

        const response = await getProfile()

        if(response.profile){

            company.value = response.profile
        }

    }

    catch(error){

        console.error(error)

        alert("Unable to load company profile.")

    }

    finally{

        loading.value = false

    }

}

onMounted(loadProfile)

</script>

<template>

<div class="company-layout">

    <CompanySidebar />

    <div class="company-content">

        <CompanyNavbar />

        <div class="container-fluid mt-4">

            <CompanyPageHeader

                title="Company Profile"

                subtitle="View your organization details"

            >

                <template #default>

                    <RouterLink

                        to="/company/profile/edit"

                        class="btn btn-success"

                    >

                        <i class="bi bi-pencil-square me-2"></i>

                        Edit Profile

                    </RouterLink>

                </template>

            </CompanyPageHeader>



            <CompanyLoading

                v-if="loading"

            />



            <CompanySectionCard

                v-else

                title="Organization Information"

            >

                <div class="row g-4">

                    <div class="col-md-6">

                        <label class="fw-bold">

                            Company Name

                        </label>

                        <p>

                            {{ company.company_name }}

                        </p>

                    </div>



                    <div class="col-md-6">

                        <label class="fw-bold">

                            Industry

                        </label>

                        <p>

                            {{ company.industry }}

                        </p>

                    </div>



                    <div class="col-md-6">

                        <label class="fw-bold">

                            Website

                        </label>

                        <a

                            :href="company.website"

                            target="_blank"

                            class="text-decoration-none"

                        >

                            {{ company.website }}

                        </a>

                    </div>



                    <div class="col-md-6">

                        <label class="fw-bold">

                            Location

                        </label>

                        <p>

                            {{ company.location }}

                        </p>

                    </div>



                    <div class="col-md-6">

                        <label class="fw-bold">

                            HR Name

                        </label>

                        <p>

                            {{ company.hr_name }}

                        </p>

                    </div>



                    <div class="col-md-6">

                        <label class="fw-bold">

                            HR Email

                        </label>

                        <p>

                            {{ company.hr_email }}

                        </p>

                    </div>



                    <div class="col-md-6">

                        <label class="fw-bold">

                            HR Phone

                        </label>

                        <p>

                            {{ company.hr_phone }}

                        </p>

                    </div>



                    <div class="col-12">

                        <label class="fw-bold">

                            Company Description

                        </label>

                        <p class="mb-0">

                            {{ company.description }}

                        </p>

                    </div>

                </div>

            </CompanySectionCard>

        </div>

    </div>

</div>

</template>

<style scoped>

.company-layout{

    display:flex;

    min-height:100vh;

    background:#F8FAFC;

}

.company-content{

    flex:1;

    display:flex;

    flex-direction:column;

}

.container-fluid{

    padding:28px;

}

label{

    display:block;

    color:#475569;

    font-size:14px;

    margin-bottom:6px;

}

p{

    background:#F8FAFC;

    border:1px solid #E2E8F0;

    border-radius:10px;

    padding:12px 15px;

    color:#0F172A;

    font-weight:500;

    margin-bottom:0;

    min-height:48px;

    display:flex;

    align-items:center;

}

a{

    display:block;

    background:#F8FAFC;

    border:1px solid #E2E8F0;

    border-radius:10px;

    padding:12px 15px;

    color:#2563EB;

    font-weight:500;

    word-break:break-all;

}

a:hover{

    background:#EFF6FF;

}

@media(max-width:992px){

.company-layout{

    flex-direction:column;

}

}

@media(max-width:768px){

.container-fluid{

    padding:18px;

}

}

</style>