import { defineStore } from "pinia";

import { login, getProfile } from "../services/auth";

export const useAuthStore = defineStore("auth", {

    state: () => ({

        token: localStorage.getItem("token"),

        user: JSON.parse(
            localStorage.getItem("user")
        ) || null

    }),

    getters: {

        isAuthenticated: (state) => !!state.token,

        role: (state) => state.user?.role

    },

    actions: {

        async login(credentials) {

            const data = await login(credentials);

            this.token = data.token;

            this.user = data.user;

            localStorage.setItem(
                "token",
                data.token
            );

            localStorage.setItem(
                "user",
                JSON.stringify(data.user)
            );
        },

        async fetchProfile() {

            return await getProfile();

        },

        logout() {

            this.token = null;

            this.user = null;

            localStorage.removeItem("token");

            localStorage.removeItem("user");

        }

    }

});