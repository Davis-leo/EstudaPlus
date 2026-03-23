import { api } from "@/lib/api";
import { SignInForm } from "@/schemas/auth";

export const signIn = async (data: SignInForm) => {
    return api<APISignInResponse>({
        endpoint: "/accounts/sign-in/",
        method: "POST",
        data
    })
}