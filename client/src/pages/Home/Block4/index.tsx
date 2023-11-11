import illustration from '../../../assets/components/home-block4-illustration.png'

import Illustration from '../../_CommonBlocks/Illustration'
import {useTranslation} from "react-i18next";

export default function Block(){
    const {t} = useTranslation();
    
    return <Illustration
        title={<>{t("page_home_block4_title")}</>}
        subTitle={<>{t("page_home_block4_text")}</>}
        content={
            <>
                {t("page_home_block4_p1")}
                <br /><br />
                {t("page_home_block4_p2")}
            </>
        }
        illustration={illustration}
    />
}