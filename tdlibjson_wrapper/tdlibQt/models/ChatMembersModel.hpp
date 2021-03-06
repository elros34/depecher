#ifndef CHATMEMBERSMODEL_HPP
#define CHATMEMBERSMODEL_HPP

#include <QtCore>
#include "tdlibQt/items/TdApi.hpp"
namespace tdlibQt {
class TdlibJsonWrapper;
class ChatMembersModel : public QAbstractListModel
{
    Q_OBJECT
    Q_PROPERTY(bool supergroupMode READ supergroupMode WRITE setSupergroupMode NOTIFY supergroupModeChanged)
    Q_PROPERTY(int count READ count NOTIFY countChanged)
public:
    explicit ChatMembersModel(QObject *parent = nullptr);
    ChatMembersModel(QObject *parent = nullptr, bool mode = false);

    bool m_supergroupMode = false;
    TdlibJsonWrapper *m_tdlibJson;
    QMap<int, int> avatarPhotoMap;
    std::vector<QSharedPointer<chatMember>> m_members;
    enum DataRoles {
        USER_ID,
        AVATAR,
        NAME,
        USERNAME,
        STATUS,
        ONLINE_STATUS,
        DELETED
    };
    enum MemberStatus {
        Administrator,
        Restricted,
        Banned,
        Creator,
        Left,
        Member
    };
    void setMembers(const std::vector<QSharedPointer<chatMember> > &members);
    Q_ENUM(MemberStatus)
    Q_INVOKABLE QVariant getProperty(int idx, const QByteArray &prop);
    int count() const;
signals:
    void supergroupModeChanged(bool supergroupMode);
    void downloadAvatar(const int fileId, const int rowIndex, const int priority) const;
    void countChanged();

private slots:
    void processFile(const QJsonObject &fileObject);
    void getFile(const int fileId, const int rowIndex, const int priority);
    void userStatusReceived(const QJsonObject &userStatusObject);
public slots:

    // QAbstractItemModel interface
    void setSupergroupMode(bool supergroupMode);

public:
    int rowCount(const QModelIndex &parent) const override;
    QVariant data(const QModelIndex &index, int role) const override;
    QHash<int, QByteArray> roleNames() const override;
    bool supergroupMode() const;
};
} // namespace tdlibQt

#endif // CHATMEMBERSMODEL_HPP
