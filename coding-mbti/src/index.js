import ReactDOM from "react-dom";
import "./index.css";
import appWrapper from "./appWrappers";
import App from "./App";
import { CometChat } from "@cometchat-pro/chat";
import { COMETCHAT_CONSTANTS } from "./chat/consts";
const propsForAppComponent = {};

var appID = COMETCHAT_CONSTANTS.APP_ID;
var region = COMETCHAT_CONSTANTS.REGION;

var appSetting = new CometChat.AppSettingsBuilder()
  .subscribePresenceForAllUsers()
  .setRegion(region)
  .build();

CometChat.init(appID, appSetting).then(
  () => {
    if (CometChat.setSource) {
      CometChat.setSource("ui-kit", "web", "reactjs");
    }
    console.log("init success");
    ReactDOM.render(
      appWrapper(App, propsForAppComponent),
      document.getElementById("root")
    );
  },
  (error) => {
    console.log("Init fail");
  }
);

export default appWrapper;
