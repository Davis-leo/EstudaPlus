"use client";

import { queryKeys } from "@/constants/query-keys";
import { getCourses } from "@/services/courses";
import { useQuery } from "@tanstack/react-query";

export const useGetCourses = (data?: object) => {
    return useQuery({
        queryKey: [queryKeys.GET_COURSES, data],
        queryFn: () => getCourses(data)
    })
}