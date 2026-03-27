"use client";

import { useSignUp } from "@/lib/mutations";
import { registerSchema, SignUpForm } from "@/schemas/auth";
import { useRouter } from "@bprogress/next/app";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { toast } from "sonner";

export const SignUpPage = () => {
    const [showPassword, setShowPassword] = useState(false)
    const [showConfirmPassword, setShowConfirmPassword] = useState(false)

    const router = useRouter()

    const { mutateAsync, isPending } = useSignUp()

    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm<SignUpForm>({
        resolver: zodResolver(registerSchema)
    })

    const onSubmit = async (data: SignUpForm) => {
        try {
            const response = await mutateAsync(data);

            if (!response.success) {
                toast.error("Erro ao criar conta.", {
                    description: response.detail
                })
                return;
            }

            toast.success("Conta criada com sucesso!", {
                description: "Redirecionando para o dashboard..."
            })

            router.push("/dashboard");
        } catch (error) {
            toast.error("Erro ao criar conta.", {
                description: "Tente novamente mais tarde."
            })
        }
    }
}