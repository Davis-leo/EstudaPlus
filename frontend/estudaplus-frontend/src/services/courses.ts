import { api } from "@/lib/api"

export const getCourses = async (data?: object) => {
    return api<APIGetCoursesResponse>({
        endpoint: "/courses/",
        data
    })
}