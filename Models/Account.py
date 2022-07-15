from Models.DatabaseManager import DatabaseManager
from hashlib import sha256


class AccessLevel:
    GUEST = 0
    BOSS = 1
    USER = 2

    def __init__(self, createTour: bool = False, deleteTour: bool = False, confirmTour: bool = False,
                 registerPassenger: bool = False,
                 modifyPassenger: bool = False, cancelRegistration: bool = False, reserveCars: bool = False):
        self.createTour = createTour
        self.deleteTour = deleteTour
        self.confirmTour = confirmTour
        self.registerPassenger = registerPassenger
        self.modifyPassenger = modifyPassenger
        self.cancelRegistration = cancelRegistration
        self.reserveCars = reserveCars


class Account:
    @classmethod
    def SignIn(cls, username: str, password: str) -> [str, AccessLevel]:
        pass_hash = sha256(password.encode()).hexdigest()
        cursor = DatabaseManager.query(
            """SELECT u.[Username], u.[Password], a.[CreateTour], a.[DeleteTour], a.[ConfirmTour], a.[RegisterPassenger], a.[ModifyPassenger], a.[CancelRegistration], a.[ReserveCars]
            FROM [UserTBL] AS u
            INNER JOIN [AccessTBL] AS a
            ON u.[AccessLevel] = a.[Id]
            WHERE [Username] = ? AND [Password] = ?""",
            username, pass_hash)
        login = cursor.fetchall()
        if len(login) != 1:
            return [None, None]
        user = login[0]
        access_level = AccessLevel(user.CreateTour, user.DeleteTour, user.ConfirmTour, user.RegisterPassenger,
                                   user.ModifyPassenger, user.CancelRegistration, user.ReserveCars)
        return [username, access_level]

    @classmethod
    def SignUp(cls, username: str, password: str, access_level: int = AccessLevel.USER) -> bool:
        # Check if username exists
        cursor = DatabaseManager.query("""SELECT [Username] FROM UserTBL WHERE [Username] = ?""", username)
        if len(cursor.fetchall()) > 0:
            return False

        pass_hash = sha256(password.encode()).hexdigest()
        cursor = DatabaseManager.execute(
            """INSERT INTO UserTBL ([Username], [Password], [AccessLevel])
            VALUES 
            (?, ?, ?)""",
            username, pass_hash, access_level
        )
        return True

    @classmethod
    def DeleteUser(cls, username):
        cursor = DatabaseManager.execute("""DELETE FROM [UserTBL] WHERE [Username] = ?""", username)
        if cursor.rowcount == 0:
            return False
        return True
