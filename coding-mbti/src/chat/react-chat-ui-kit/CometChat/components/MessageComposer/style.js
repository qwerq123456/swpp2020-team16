export const chatComposerStyle = (props) => {

    return {
        padding: "14px 16px",
        backgroundColor: `${props.theme.backgroundColor.white}`,
        zIndex: "1",
        order: "3",
        position: "relative",
        flex: "none",
        minHeight: "105px",
    }
}

export const editPreviewContainerStyle = (props, keyframes) => {

    const slideAnimation = keyframes`
    from {
        bottom: -60px
    }
    to {
        bottom: 0px
    }`;

    return {
        padding: "7px",
        backgroundColor: `${props.theme.backgroundColor.white}`,
        borderColor: `${props.theme.borderColor.primary}`,
        borderWidth: "1px 1px 1px 5px",
        borderStyle: "solid",
        color: `${props.theme.color.helpText}`,
        fontSize: "13px",
        animation: `${slideAnimation} 0.5s ease-out`,
        position: "relative",
    }
}

export const previewHeadingStyle = () => {

    return {
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between"
    }
}

export const previewTextStyle = () => {

    return {
        padding: "5px 0",
    }
}

export const previewCloseStyle = (img) => {

    return {
        width: "24px",
        height: "24px",
        borderRadius: "50%",
        background: `url(${img}) center center no-repeat`,
        cursor: "pointer",
    }
}

export const composerInputStyle = () => {

    return {
        display: "flex",
        width: "100%",
        flexDirection: "row",
        alignItems: "flex-end",
        position: "relative",
        zIndex: "2",
        padding: "0",
        minHeight: "85px",
    }
}

export const inputInnerStyle = (props) => {

    return {
        flex: "1 1 auto",
        position: "relative",
        outline: "none",
        borderRadius: "8px",
        border: `1px solid ${props.theme.borderColor.primary}`,
        backgroundColor: `${props.theme.backgroundColor.white}`,
        display: "flex",
        flexDirection: "column",
        width: "100%",
        minHeight: "85px",
    }
}

export const messageInputStyle = (disabled) => {

    const disabledState = (disabled) ? {
        pointerEvents : "none",
        opacity: "0.4"
    } : {};

    return {
        width: "100%",
        fontSize: "15px",
        lineHeight: "20px",
        fontWeight: "400",
        padding: "15px 10px",
        outline: "none",
        overflowX: "hidden",
        overflowY: "auto",
        position: "relative",
        whiteSpace: "pre-wrap",
        wordWrap: "break-word",
        zIndex: "1",
        minHeight: "50px",
        maxHeight: "100px",
        userSelect: "text",
        ...disabledState,
        '&:empty:before': {
            content: "attr(placeholder)",
            color: "rgb(153, 153, 153)",
            pointerEvents: "none",
            display: "block", /* For Firefox */
        }
    }
}

export const inputStickyStyle = (props) => {

    return {
        padding: "7px 10px",
        height: "35px",
        borderTop: `1px solid ${props.theme.borderColor.primary}`,
        backgroundColor: `${props.theme.backgroundColor.grey}`,
        display: "flex",
        justifyContent: "space-between",
    }
}

export const stickyAttachmentStyle = () => {

    return {
        display: "flex",
    }
}

export const attachmentIconStyle = (img) => {

    return {
        margin: "auto 0",
        ' > span': {
            display: "inline-block",
            width: "20px",
            height: "20px",
            background: `url(${img}) center center no-repeat`,
            cursor: "pointer",
        }
    }
}

export const filePickerStyle = (state) => {

    const active = (state.showFilePicker) ? {
        width: "120px",
        opacity: "1",
        margin: "auto 10px",
    } : {};

    return {
        left: "0",
        bottom: "0",
        position: "relative",
        width: "0",
        borderRadius: "8px",
        overflow: "hidden",
        zIndex: "1",
        textAlign: "center",
        opacity: "0",
        transition: "width 0.5s linear",
        ...active
    }
}

export const fileListStyle = () => {

    return {
        width: "100%",
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
    }
}

export const fileItemStyle = (props, img) => {

    const icon = {
        background: `url(${img}) no-repeat 100% 100%`,
    }

    return {
        width: "21px",
        height: "21px",
        backgroundColor: `${props.theme.backgroundColor.secondary}`,
        cursor: "pointer",
        ' > input': {
            display: "none",
        },
        ...icon
    }
}

export const stickyButtonStyle = () => {

    return {
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        "div:not(:first-of-type)": {
            marginLeft: "5px",
        },
        "div:not(:last-of-type)": {
            marginRight: "5px"
        }
    }
}

export const emojiButtonStyle = () => {

    return {
        width: "20px",
        height: "20px",
        cursor: "pointer",
    }
}

export const sendButtonStyle = () => {

    return {
        width: "20px",
        height: "20px",
        cursor: "pointer",
    }
}

export const reactionBtnStyle = () => {

    return {
        cursor: "pointer",
        width: "20px",
        height: "20px",
    }
}

export const stickerBtnStyle = () => {

    return {
        cursor: "pointer",
        width: "20px",
        height: "20px",
    }
}