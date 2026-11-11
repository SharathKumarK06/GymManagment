import streamlit as st
from gym_view import GymManagement

gym = GymManagement()
add_member, view_member, update_member, delete_member = st.tabs([
    "Add Member", "View Member", "Update Member", "Delete Member"
])

gym_plan = ["1 Month", "2 Month", "3 Month", "6 Month",
    "8 Month", "1 Year"
]

def get_plan_index(plan):
    for i, p in enumerate(gym_plan):
        if plan == p:
            return i
    return None

with add_member:
    st.title("Add member")
    name = st.text_input("Name:")
    place = st.text_input("Place:")
    mobile = st.text_input("Mobile:")
    plan = st.selectbox("Plan:", gym_plan, key="add_group")
    fee = st.text_input("Fee:")
    join_date = st.date_input("Join date:")
    if st.button("Submit", key="add_btn"):
        gym.post(
            name=name, place=place, mobile=mobile,
            plan=plan, fee=fee, join_date=join_date
        )
        st.success("Member added successfully.")
        st.rerun()

with view_member:
    st.title("Add member")
    records = gym.get()
    if records:
        st.table(records)
    else:
        st.error("Error: no members found.")

with update_member:
    st.title("Update member")
    records = gym.get()
    if records:
        record_ids = [r[0] for r in records]
        rec_id = st.selectbox("Record Id:", record_ids, key="update_group")
        record = gym.retreive(rec_id)
        name = st.text_input("Name:", record[1])
        place = st.text_input("Place:", record[2])
        mobile = st.text_input("Mobile:", record[3])

        plan = st.selectbox("Plan:", gym_plan, gym_plan.index(record[4]),
            key="update_plan_group"
        )
        fee = st.text_input("Fee:", record[5])
                
        if st.button("Submit", key="update_btn"):
            status, message = gym.put(
                id=rec_id, name=name, place=place, mobile=mobile, plan=plan,
                fee=fee
            )
            if status:
                st.success("Member details updated successfully.")
                st.rerun()
            else:
                st.error("Error:", message)
                st.rerun()
    else:
        st.warning("No members found.")
        st.rerun()

with delete_member:
    st.title("Delete member")
    records = gym.get()
    if records:
        record_ids = [r[0] for r in records]
        rec_id = st.selectbox("Record Id:", record_ids, key="delete_group")
        record = gym.retreive(rec_id)
        st.text(f"Name: {record[1]}")
        st.text(f"Place: {record[2]}")
        st.text(f"Mobile: {record[3]}")
        st.text(f"Plan: {record[4]}")
        st.text(f"Fee: {record[5]}")
        st.text(f"Join date: {record[6]}")

        if st.button("Delete"):
            status, message = gym.delete(record[0])
            if status:
                st.success(message)
                st.rerun()
            else:
                st.error(message)
                st.rerun()

    else:
        st.warning("No members found")

