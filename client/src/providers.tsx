import { Suspense } from "react";
import { Provider } from "react-redux";
import { useTranslation } from "react-i18next";
import { QueryClient, QueryClientProvider } from "react-query"
import { LocalizationProvider } from "@mui/x-date-pickers"
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs"
import "dayjs/locale/ru"


import { store } from "./app/store";


const queryClient = new QueryClient();

export default function Providers(props: {
    children: React.ReactNode
}) {
    const {i18n} = useTranslation()

    return <QueryClientProvider client={queryClient}>
        <Provider store={store}>
            <LocalizationProvider dateAdapter={AdapterDayjs} adapterLocale={i18n.language}>
                <Suspense fallback={'...Loading'}>
                    {props.children}
                </Suspense>
            </LocalizationProvider>
        </Provider>
    </QueryClientProvider>
}