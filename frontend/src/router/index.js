import {

createRouter,

createWebHistory

} from "vue-router";

import Login from "../pages/auth/Login.vue";

import StudentRegister from "../pages/auth/StudentRegister.vue";

import CompanyRegister from "../pages/auth/CompanyRegister.vue";

// Student

import Dashboard from "../pages/student/Dashboard.vue"
import Profile from "../pages/student/Profile.vue"
import StudentDrives from "../pages/student/Drives.vue"
import StudentApplications from "../pages/student/Applications.vue"
import History from "../pages/student/History.vue"
import StudentDriveDetails from "../pages/student/DriveDetails.vue"
import EditProfile from "../pages/student/EditProfile.vue"
import ExportApplications from "../pages/student/ExportApplications.vue"

// Company

import CompanyDashboard from "../pages/company/Dashboard.vue"
import CompanyProfile from "../pages/company/Profile.vue"
import CompanyEditProfile from "../pages/company/EditProfile.vue"
import CreateDrive from "../pages/company/CreateDrive.vue"
import ManageDrives from "../pages/company/ManageDrives.vue"
import DriveApplications from "../pages/company/DriveApplications.vue"
import CompanyStudentDetails from "../pages/company/StudentDetails.vue"
import SelectedStudents from "../pages/company/SelectedStudents.vue"

// Admin

import AdminDashboard from "../pages/admin/Dashboard.vue"
import Companies from "../pages/admin/Companies.vue"
import Students from "../pages/admin/Students.vue"
import AdminStudentDetails from "../pages/admin/StudentDetails.vue"
import AdminDrives from "../pages/admin/Drives.vue"
import AdminDriveDetails from "../pages/admin/DriveDetails.vue"
import AdminApplications from "../pages/admin/Applications.vue"
import Reports from "../pages/admin/Reports.vue"
import AdminExportCSV from "../pages/admin/ExportCSV.vue"
import Settings from "../pages/admin/Settings.vue"
import Statistics from "../pages/admin/Statistics.vue"

const routes=[

{

path:"/",

redirect:"/login"

},

{

path:"/login",

component:Login

},

{

path:"/register/student",

component:StudentRegister

},

{

path:"/register/company",

component:CompanyRegister

},

{
    path: "/student/dashboard",
    component: Dashboard
},
{
    path: "/student/profile",
    component: Profile
},
{
    path: "/student/drives",
    component: StudentDrives
},
{
    path: "/student/applications",
    component: StudentApplications
},
{
    path: "/student/history",
    component: History
},
{
    path: "/student/drives/:id",
    component: StudentDriveDetails
},
{
    path: "/student/export",
    component: ExportApplications,
    meta: {
        requiresAuth: true,
        role: "STUDENT"
    }
},
{
path:"/student/profile/edit",
component:EditProfile
},
{
    path: "/company/dashboard",
    component: CompanyDashboard
},
{
    path: "/company/profile",
    component: CompanyProfile
},
{
    path: "/company/profile/edit",
    component: CompanyEditProfile
},
{
    path: "/company/create-drive",
    component: CreateDrive
},
{
    path: "/company/drives",
    component: ManageDrives
},
{
    path: "/company/drives/:id/applications",
    component: DriveApplications
},
{
    path: "/company/student/:id",
    component: CompanyStudentDetails
},
{
    path: "/company/selected",
    component: SelectedStudents
},
{
    path:"/admin/dashboard",
    component:AdminDashboard
},
{
    path:"/admin/companies",
    component:Companies
},
{
    path:"/admin/students",
    component:Students
},
{
    path: "/admin/student/:id",
    component: AdminStudentDetails
},
{
    path: "/admin/drives",
    component: AdminDrives
},
{
    path: "/admin/drives/:id",
    component: AdminDriveDetails
},
{
    path:"/admin/applications",
    component:AdminApplications
},
// {
//     path:"/admin/notifications",
//     name:"AdminNotifications",
//     component: AdminNotifications
// },

// Admin
{
    path: "/admin/notifications",
    name: "AdminNotifications",
    component: () => import("../pages/admin/Notifications.vue"),
    meta: {
        requiresAuth: true,
        role: "ADMIN"
    }
},

// Student
{
    path: "/student/notifications",
    name: "StudentNotifications",
    component: () => import("../pages/student/Notifications.vue"),
    meta: {
        requiresAuth: true,
        role: "STUDENT"
    }
},

// Company
{
    path: "/company/notifications",
    name: "CompanyNotifications",
    component: () => import("../pages/company/Notifications.vue"),
    meta: {
        requiresAuth: true,
        role: "COMPANY"
    }
},
{
    path:"/admin/reports",
    component:Reports
},
{
    path:"/admin/export",
    component:AdminExportCSV
},

{
    path:"/admin/settings",
    component:Settings
},
{
    path: "/admin/statistics",
    component: Statistics
},

];

const router=createRouter({

history:createWebHistory(),

routes

});

router.beforeEach((to) => {

    const token = localStorage.getItem("token");

    const user = JSON.parse(
        localStorage.getItem("user")
    );

    const role = user?.role;

    if (to.meta.requiresAuth && !token) {
        return "/login";
    }

    if (to.meta.role && role !== to.meta.role) {
        return "/login";
    }

    return true;
});

export default router;
