# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2026)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

import streamlit as st

dir_path = Path(__file__).parent


# Note that this needs to be in a method so we can have an e2e playwright test.
def run() -> None:
    page = st.navigation(
        {
            "Pages": [
                st.Page(
                    dir_path / "hello.py", title="Hello", icon=":material/waving_hand:"
                ),
                st.Page(
                    dir_path / "mychatbot.py",
                    title="ChatBot",
                    icon=":material/chat:",
                ),
				st.Page(
                    dir_path / "Python Assignment8_gopikrishna.py",
                    title="Regulur Expression",
                    icon="🔎",
                ),
                st.Page(
                    dir_path / "studentresultnew.py",
                    title="Student Result",
                    icon="🎯",
                ),
				st.Page(
                    dir_path / "Uploading Files.py",
                    title="Uploading Files",
                    icon=":material/upload:",
                ),
                st.Page(
                    dir_path / "Assignment10_gopikrishna.py",
                    title="Automated Multi-Sheet Excel",
                    icon="🔗",
                ),
		
            ]
        }
    )
    page.run()


if __name__ == "__main__":
    run()
